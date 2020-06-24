# -*- encoding: utf-8 -*-
'''
@Filename    : baseLink.py
@Datetime    : 2020/06/22 19:47:47
@Author      : Joe-Bu
@version     : 1.0
@description : Base Link Class.
'''

import os
import sys


class baseLink:
    '''
    Base Emission Data Link Class.
    '''
    def __init__(self, name, this_time):
        self.name = name
        self.this_time = this_time

    def gen_sflink(self, src: str, dst: str) -> str:
        '''
        Generate soft link class method
        '''
        assert os.path.exists(src)
        os.symlink(src, dst)
        assert os.path.exists(dst)

        return dst

    def checkdir(self, path):
        '''
            Check dirname.
        '''
        if not os.path.exists(path):
            os.makedirs(path)

        assert os.path.exists(path)

    def _show_url(self, url):
        '''
            Print src|dst urls.
        '''
        assert isinstance(url, str)
        print(url)
        