#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import sys
from PIL import Image
from PIL import ImageColor

from dpiutil import DpiType
from dpiutil import DpiUtil
from settings import Settings

def main_is_frozen():
    # for new py2exe
    return (hasattr(sys, "frozen"))


def get_app_dir_path():
    if main_is_frozen():
        return os.path.abspath(os.path.dirname(sys.executable))
    return os.path.abspath(os.path.dirname(sys.argv[0]))


def generate_colored_image(src_image_file_path, fg_color_str):

    fg_color = ImageColor.getcolor(fg_color_str, 'RGBA')

    src_image = Image.open(src_image_file_path)

    src_img_alpha = None

    if (src_image.mode in ('RGBA', 'LA') or
        (src_image.mode == 'P' and 'transparency' in src_image.info)):
        src_img_alpha = src_image.convert('RGBA').split()[-1]

    dst_img = Image.new('RGBA', src_image.size, fg_color)

    if src_img_alpha:
        dst_img.putalpha(src_img_alpha)

    return dst_img


def generate_images(src_image, mdpi_image_width, dst_dir_path, src_image_file_name):
    dpi_types = [DpiType.mdpi, DpiType.hdpi, DpiType.xhdpi, DpiType.xxhdpi, DpiType.xxxhdpi]

    for dpi_type in dpi_types:
        w = DpiUtil.calculate_image_width(mdpi_image_width, dpi_type)
        h = src_image.size[1] * w / src_image.size[0]

        dst_img = src_image.resize((w, h), Image.LANCZOS)

        path = os.path.join(dst_dir_path, DpiUtil.get_image_dir_name(dpi_type))
        if not os.path.exists(path):
            os.makedirs(path)

        path = os.path.join(path, src_image_file_name)

        dst_img.save(path)


def main():
    settings_file_path = os.path.join(get_app_dir_path(), Settings.SETTINGS_FILE_NAME)

    settings = Settings()

    if not os.path.exists(settings_file_path):
        print("Setting file \"" + Settings.SETTINGS_FILE_NAME + "\" is not found.")
        return

    settings.load(settings_file_path)

    src_image_file_paths = sys.argv[1:]
    if not src_image_file_paths:
        print("Pass input image files as arguments.")
        return

    dst_dir_path = settings.dst_dir_path
    if dst_dir_path and not os.path.exists(dst_dir_path):
        os.makedirs(dst_dir_path)

    for src_image_file_path in src_image_file_paths:
        src_image_file_name = os.path.basename(src_image_file_path)
        if settings.fg_color_str:
            src_image = generate_colored_image(src_image_file_path, settings.fg_color_str)
        else:
            src_image = Image.open(src_image_file_path)
        generate_images(src_image, settings.mdpi_image_width, settings.dst_dir_path, src_image_file_name)


if __name__ == '__main__':

    main()

    raw_input("Press any key.")