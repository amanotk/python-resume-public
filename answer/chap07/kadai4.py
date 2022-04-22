#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import json
import argparse
import datetime
import chardet
from urllib import request

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# Open-Meteo
openmeteo = r'https://api.open-meteo.com/v1/forecast?latitude=35.6785&longitude=139.6823&hourly=temperature_2m,precipitation,windspeed_10m,winddirection_10m&windspeed_unit=ms&timezone=Asia%2FTokyo&past_days=1'


def parse_args():
    parser = argparse.ArgumentParser(description=\
                                     "Plot weather variables obtained from Open-Meteo "
                                     "https://open-meteo.com/")
    parser.add_argument('-s', '--save', type=str, default=None,
                        help='filename for save')
    args = parser.parse_args()

    return args.save


def get_url_contents(url):
    response = request.urlopen(url)
    stream   = response.read()
    # chardet.detectで文字コードを推測
    encoding = chardet.detect(stream).get('encoding')
    return stream.decode(encoding)


def plot(contents, variables, save=None):
    # jsonとして読み込み，時系列データを取り出す
    obj = json.loads(contents)
    dat = obj['hourly']

    # 時間
    time = np.array(dat['time'], np.datetime64)
    tnow = np.datetime64(datetime.datetime.now())

    # データのプロット
    n = len(variables)

    fig, axs = plt.subplots(n, 1, figsize=(10, 8))
    fig.subplots_adjust(left=0.1, bottom=0.05, right=0.95, top=0.95,
                        wspace=0.2, hspace=0.2)

    for i in range(n):
        # プロット
        label = variables[i]['label']
        y = np.array(dat[variables[i]['name']])
        m = np.size(y)
        plt.sca(axs[i])
        plt.plot(time[0:m], y[0:m])

        # 図の見た目を整形
        ymin, ymax = axs[i].get_ylim()
        plt.vlines(tnow, ymin, ymax, colors='r', linestyle='dashed')
        axs[i].set_xlim(time[0], time[-1])
        axs[i].set_ylim(ymin, ymax)
        axs[i].set_ylabel(label)
        axs[i].grid()

    # 緯度・経度を表示
    lat = obj['latitude']
    lon = obj['longitude']
    plt.suptitle('Latitude = {}, Longitude = {}'.format(lat, lon))

    if save is None:
        # 表示
        plt.show()
    else:
        # ファイルに保存
        plt.savefig(save)


if __name__ == '__main__':
    # プロットする変数とラベル
    variables = [
        {'name' : 'temperature_2m'   , 'label' : 'Temperature [deg]'},
        {'name' : 'precipitation'    , 'label' : 'Precipitation [mm]'},
        {'name' : 'windspeed_10m'    , 'label' : 'Wind speed [m/s]'},
        {'name' : 'winddirection_10m', 'label' : 'Wind Direction [deg]'},
    ]
    save = parse_args()
    contents = get_url_contents(openmeteo)
    plot(contents, variables, save)
