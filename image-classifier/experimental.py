import pathlib
import os
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf


dataset_url = "https://1drv.ms/u/s!AkGrCMoO9SmmjftyREzLbHuIINZNYA?e=jvapfa"
data_dir = tf.keras.utils.get_file('ai-images-dataset', origin=dataset_url, untar=True)
data_dir = pathlib.Path(data_dir)

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)
