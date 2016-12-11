#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum

class DpiType(Enum):
    ldpi = 0
    mdpi = 1
    hdpi = 2
    xhdpi = 3
    xxhdpi = 4
    xxxhdpi = 5


class DpiUtil:
    def __init__(self):
        pass

    @staticmethod
    def calculate_image_width(mdpi_image_width, dpi_type):
        if dpi_type == DpiType.ldpi:
            return mdpi_image_width * 3 / 4
        elif dpi_type == DpiType.mdpi:
            return mdpi_image_width
        elif dpi_type == DpiType.hdpi:
            return mdpi_image_width * 3 / 2
        elif dpi_type == DpiType.xhdpi:
            return mdpi_image_width * 2
        elif dpi_type == DpiType.xxhdpi:
            return mdpi_image_width * 3
        elif dpi_type == DpiType.xxxhdpi:
            return mdpi_image_width * 4
        else:
            return mdpi_image_width

    @staticmethod
    def get_image_dir_name(dpi_type):
        if dpi_type == DpiType.ldpi:
            return 'drawable-ldpi'
        elif dpi_type == DpiType.mdpi:
            return 'drawable-mdpi'
        elif dpi_type == DpiType.hdpi:
            return 'drawable-hdpi'
        elif dpi_type == DpiType.xhdpi:
            return 'drawable-xhdpi'
        elif dpi_type == DpiType.xxhdpi:
            return 'drawable-xxhdpi'
        elif dpi_type == DpiType.xxxhdpi:
            return 'drawable-xxxhdpi'
        else:
            return 'drawable-mdpi'

