#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


class Settings:

    SETTINGS_FILE_NAME = 'settings.json'

    def __init__(self):
        # 出力先ディレクトリーのパス
        self.dst_dir_path = ''

        # mdpiにおける幅
        self.mdpi_image_width = 24

        # フォアグラウンドカラー(空文字列だと塗らない)
        self.fg_color_str = ''

    def save(self, file_path):
        settings_json = {}
        settings_json['dstDirPath'] = self.dst_dir_path
        settings_json['mdpiImageWidth'] = self.mdpi_image_width
        settings_json['fgColorStr'] = self.fg_color_str

        with open(file_path, 'w') as f:
            json.dump(settings_json, f)

    def load(self, file_path):
        with open(file_path, 'r') as f:
            settings_json = json.load(f)

        self.dst_dir_path = settings_json['dstDirPath']
        self.mdpi_image_width = settings_json['mdpiImageWidth']
        self.fg_color_str = settings_json['fgColorStr']

