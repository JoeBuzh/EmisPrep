# -*- encoding: utf-8 -*-
'''
@Filename    : wrfclinker.py
@Datetime    : 2020/06/23 15:55:05
@Author      : Joe-Bu
@version     : 1.0
'''

import os
import sys
from datetime import datetime, timedelta

import numpy as np
import xarray as xr

from links.baselink import baseLink


class wrfcLink(baseLink):
    '''
    Wrf-Chem Emission Data Pre_processing Class.
        Function
            0. Modify src wrfchemi_d0{1|2|3}_2018_MM_15_HH:00:00;
            1. rename filename
            2. change 'Times'
            3. Copy dst to output
    '''
    def __init__(self, name: str, this_time: datetime, cfg: dict, in_path: str, out_path: str):
        '''
        Init.
        '''
        super().__init__(name=name, this_time=this_time)
        # base cfg
        # TODO: dict loop
        self.base_year = cfg.get('base_year')
        self.base_day = cfg.get('base_day')
        self.domains = cfg.get('domains')
        self.dt_format = cfg.get('dt_format')
        self.pred_seq = cfg.get('pred_seq')
        # data dir
        self.data_in = os.path.join(in_path, self.name)
        self.data_out = os.path.join(out_path, self.name)

    def _check_domain(self):
        '''
            Domain Loop.
        '''
        assert isinstance(self.domains, list) and len(self.domains)>=1

        for domain in self.domains:
            self._check_time(domain)

    def _check_time(self, domain):
        '''
            Predict Sequence Loop.
        '''
        start = self.this_time
        end = start + timedelta(hours=self.pred_seq)

        while start <= end:
            src_file = 'wrfchemi_d0{0}_{1}-{2}-{3}_{4}:00:00'.format(
                domain, 
                self.base_year, 
                start.strftime("%m"),
                self.base_day,
                start.strftime("%H")
            )
            dst_file = 'wrfchemi_d0{0}_{1}'.format(
                domain,
                start.strftime(self.dt_format)
            )
            src = os.path.join(self.data_in, src_file)
            dst = os.path.join(self.data_out, dst_file)

            # workflow
            self._gen_file(src, dst, start)

            start += timedelta(hours=1)

    def _gen_file(self, src: str, dst: str, dt: datetime):
        '''
            Generate dst file based on src file.
                0. Open src file
                1. Change varibales-Times
                2. Rename filename and save to dst_file.
                3. Make sure dst file exist.
        '''
        assert os.path.exists(src)

        dataset = xr.open_dataset(src)
        dt_new = dt.strftime(self.dt_format)
        dataset['Times'].values[0] = dt_new.encode('utf-8')
        dataset.to_netcdf(dst)

        assert os.path.exists(dst)

    def _step_control(self):
        '''
        Inner process control.
            0. Check output dir mainly focus on ${output}/${model_name}/${date}.
            1. Execute domain loop within predict sequence loop.
        '''
        # self.tmp_dst = os.path.join(self.data_out, self.this_time.strftime("%Y%m%d"))
        self.checkdir(self.data_out)
        self._check_domain()