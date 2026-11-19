#「何を実行するか」を明示する場所
# SPDX-FileCopyrightText: 2026 Kazuki Nakatomi
# SPDX-License-Identifier: BSD-3-Clause
import os                  #追加。OSの機能のパッケージ
from glob import glob      #追加。グロブ（ワイルドカード）を扱う関数
from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),  #追加
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kazuki Nakatomi',
    maintainer_email='u7610366@gmail.com',
    description='Package for practice',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',      #talker.pyのmain関数をtalkerという名前で
            'listener = mypkg.listener:main', #後で使うので書いておいてコメントアウト(解除済み)
        ],
    },
)
