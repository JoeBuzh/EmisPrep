# -*- encoding: utf-8 -*-
'''
@Filename    : cfg.py
@Datetime    : 2020/06/22 19:17:36
@Author      : Joe-Bu
@version     : 1.0
'''

import os

proj_dir = r'/public/home/buzh/EmisPrep'
paths = {
    'input_dir': os.path.join(proj_dir, 'input'),
    'output_dir': os.path.join(proj_dir, 'output')
}

naqp_cfg = {
    'name': 'naqp',
    'base_year': 2018,
    'base_day': 15,
    'domains': [1, 2, 3],
    'dt_format': '%Y%m%d%H',
    'pred_seq': 24
}

osam_cfg = {
    'name': 'osam',
    'base_year': 2018,
    'base_day': 15,
    'domains': [1, 2, 3],
    'dt_format': '%Y%m%d%H',
    'pred_seq': 5,
    'source': ['agriculture', 'biogenic', 'industry', 'others', 
               'power', 'residential', 'total', 'transportation']
}

wrfc_cfg = {
    'name': 'wrfc',
    'base_year': 2018,
    'base_day': 15,
    'domains': [1, 2],
    'dt_format': '%Y-%m-%d_%H:00:00',
    'pred_seq': 3
}

cmaq_cfg = {
    'name': 'cmaq',
    'domains': [1, 2, 3],
    'dt_format': '%Y%j%H',
    'pred_seq': 2
}

cmax_cfg = {
    'name': 'cmax',
    'domains': [1, 2, 3],
    'dt_format': '%Y%m%d%H',
    'pred_seq': 5
}