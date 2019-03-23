#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function
import tensorflow as tf
from tensorflow.python.ops import control_flow_ops

slim = tf.contrib.slim

_R_MEAN = 123.68
_G_MEAN = 116.78
_B_MEAN = 103.94

_RESIZE_SIDE_MIN = 256
_RESIZE_SIDE_MAX = 512


def _crop(image, offset_height, offset_width, crop_height, crop_width):
    original_shape = tf.shape(image)

    rank_assertion = tf.Assert(
        tf.equal(tf.rank(image), 3),
        ['Rank of image must be equal to 3.'])
    cropped_shape = control_flow_ops.with_dependencies(
        [rank_assertion],
        tf.stack([crop_height, crop_width, original_shape[2]]))

    # print(original_shape[0], crop_height)
    # print(original_shape[1], crop_width)
    size_assertion = tf.Assert(
        tf.logical_and(
            tf.greater_equal(original_shape[0], crop_height),
            tf.greater_equal(original_shape[1], crop_width)),
        ['Crop size greater than the image size.'])

    offsets = tf.to_int32(tf.stack([offset_height, offset_width, 0]))

    # Use tf.slice instead of crop_to_bounding box as it accepts tensors to
    # define the crop size.
    image = control_flow_ops.with_dependencies(
        [size_assertion],
        tf.slice(image, offsets, cropped_shape))
    return tf.reshape(image, cropped_shape)

def _central_crop(image_list, crop_height, crop_width):
    outputs = []
    for image in image_list:
        image_height = tf.shape(image)[0]
        image_width = tf.shape(image)[1]

        offset_height = (image_height - crop_height) / 2
        offset_width = (image_width - crop_width) / 2
        outputs.append(_crop(image, offset_height, offset_width,
                             crop_height, crop_width))
    return outputs


def _mean_image_subtraction(image, means):

    if image.get_shape().ndims != 3:
        raise ValueError('Input must be of size [height, width, C>0]')
    num_channels = image.get_shape().as_list()[-1]
    if len(means) != num_channels:
        raise ValueError('len(means) must match the number of channels')

    channels = tf.split(image, num_channels, 2)
    for i in range(num_channels):
        channels[i] -= means[i]
    return tf.concat(channels, 2)

def _smallest_size_at_least(height, width, target_height, target_width):

    target_height = tf.convert_to_tensor(target_height, dtype=tf.int32)
    target_width = tf.convert_to_tensor(target_width, dtype=tf.int32)

    height = tf.to_float(height)
    width = tf.to_float(width)
    target_height = tf.to_float(target_height)
    target_width = tf.to_float(target_width)

    scale = tf.cond(tf.greater(target_height / height, target_width / width),
                    lambda: target_height / height,
                    lambda: target_width / width)
    new_height = tf.to_int32(tf.round(height * scale))
    new_width = tf.to_int32(tf.round(width * scale))
    return new_height, new_width


def _aspect_preserving_resize(image, target_height, target_width):

    target_height = tf.convert_to_tensor(target_height, dtype=tf.int32)
    target_width = tf.convert_to_tensor(target_width, dtype=tf.int32)

    shape = tf.shape(image)
    height = shape[0]
    width = shape[1]
    new_height, new_width = _smallest_size_at_least(height, width, target_height, target_width)
    image = tf.expand_dims(image, 0)
    resized_image = tf.image.resize_bilinear(image, [new_height, new_width],
                                             align_corners=False)
    resized_image = tf.squeeze(resized_image)
    resized_image.set_shape([None, None, 3])
    return resized_image

def preprocess_for_eval(image, output_height, output_width, resize_side):
    image = _aspect_preserving_resize(image, output_height, output_width)
    image = _central_crop([image], output_height, output_width)[0]
    image.set_shape([output_height, output_width, 3])
    image = tf.to_float(image)
    return _mean_image_subtraction(image, [_R_MEAN, _G_MEAN, _B_MEAN])


def preprocess_image(image, output_height, output_width, resize_side_min=_RESIZE_SIDE_MIN,resize_side_max=_RESIZE_SIDE_MAX,):
    return preprocess_for_eval(image, output_height, output_width,resize_side_min)
