# -*- encoding: utf-8 -*-
'''
@Filename    : main.py
@Datetime    : 2020/06/22 19:59:07
@Author      : Joe-Bu
@version     : 1.0
'''

import os
import sys
from datetime import datetime, timedelta

import numpy as np
import xarray as xr

from links.naqplinker import naqpLink
from links.wrfclinker import wrfcLink
from links.osamlinker import osamLink
from links.cmaqlinker import cmaqLink
from cfg import paths, naqp_cfg, wrfc_cfg, osam_cfg, cmaq_cfg, cmax_cfg


def link_naqp(naqp_cfg, this_time, input_dir, output_dir):
    '''
    Link naqp main.
    '''
    name = naqp_cfg.get('name')
    naqp_link = naqpLink(name, this_time, naqp_cfg, input_dir, output_dir)
    # print(naqp_link.data_in)
    # print(naqp_link.data_out)
    naqp_link._step_control()


def link_osam(osam_cfg, this_time, input_dir, output_dir):
    '''
    Link osam main
    '''
    name = osam_cfg.get('name')
    osam_link = osamLink(name, this_time, osam_cfg, input_dir, output_dir)
    osam_link._step_control()


def link_wrfc(wrfc_cfg, this_time, input_dir, output_dir):
    '''
    Link wrfc main.
    '''
    name = wrfc_cfg.get('name')
    wrfc_link = wrfcLink(name, this_time, wrfc_cfg, input_dir, output_dir)
    wrfc_link._step_control()


def link_cmaq(cmaq_cfg, this_time, input_dir, output_dir):
    '''
    Link cmaq main.
    '''
    name = cmaq_cfg.get('name')
    cmaq_link = cmaqLink(name, this_time, cmaq_cfg, input_dir, output_dir)
    cmaq_link._step_control()


def link_cmax(cmaq_cfg, this_time, input_dir, output_dir):
    '''
    Link cmax main.
    '''
    pass


def main():
    '''
    Main.
    '''
    # time
    # this_time = datetime.now()
    this_time = datetime(2020, 6, 26, 14, 0)
    # dir
    input_dir = paths.get('input_dir')
    output_dir = paths.get('output_dir')
    # link
    link_naqp(naqp_cfg, this_time, input_dir, output_dir)
    link_wrfc(wrfc_cfg, this_time, input_dir, output_dir)
    link_osam(osam_cfg, this_time, input_dir, output_dir)
    link_cmaq(cmaq_cfg, this_time, input_dir, output_dir)
    # link_cmax(cmax_cfg, this_time, input_dir, output_dir)


if __name__ == "__main__":
    main()
