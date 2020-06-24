# -*- encoding: utf-8 -*-
'''
@Filename    : cmaqlinker.py
@Datetime    : 2020/06/24 10:56:36
@Author      : Joe-Bu
@version     : 1.0
'''

import os
import sys
from datetime import datetime, timedelta

import numpy as np
import xarray as xr

from links.baselink import baseLink


class cmaqLink(baseLink):
    '''
    Cmaq Emission Data Pre_processing Class.
    '''
    def __init__(self, name: str, this_time: datetime, cfg: dict, in_path: str, out_path: str):
        '''
        Init instance.
        '''
        super().__init__(name=name, this_time=this_time)
        # cfg
        self.domains = cfg.get('domains')
        self.dt_format = cfg.get('dt_format')
        self.pred_seq = cfg.get('pred_seq')
        # data dir
        self.data_in = os.path.join(in_path, self.name)
        self.data_out = os.path.join(out_path, self.name)

    def __read_nc(self, filename: str) -> xr.Dataset:
        '''
            Read *.nc *.ncf file func.
            filename: abspath.
        '''
        print(filename)
        assert os.path.exists(filename)

        data = xr.open_dataset(filename)
        return data

    def __write_nc(self, data: xr.Dataset, filename: str):
        '''
            Write .nc func.
            filename: abspath.
        '''
        print(filename)
        data.to_netcdf(filename, mode='w', format="NETCDF3_CLASSIC")
        
        assert os.path.exists(filename)

    def _check_domain(self):
        '''
            Domain Loop.
        '''
        assert isinstance(self.domains, list) and len(self.domains)>=1

        for domain in self.domains:
            self._concat_time(domain)

    def _concat_time(self, domain):
        '''
            Predict Sequence Loop.
        '''
        start = self.this_time
        end = start + timedelta(hours=self.pred_seq)

        sdate = start.strftime("%Y%j")
        stime = start.strftime("%H0000")
        data_list = []
        while start <= end:
            src_file = 'EM_D{0}_{1}.ncf'.format(domain, start.strftime(self.dt_format))
            src = os.path.join(self.data_in, src_file)
            data = self.__read_nc(src)
            data_list.append(data)

            start += timedelta(hours=1)
        # concat
        data_all = xr.concat(data_list, dim='TSTEP')
        data_all.attrs['SDATE'] = np.int32(sdate)
        data_all.attrs['STIME'] = np.int32(stime)
        # save
        dst_file = 'EM_D{0}_{1}.ncf'.format(domain, self.this_time.strftime(self.dt_format))
        dst = os.path.join(self.data_out, dst_file)
        self.__write_nc(data_all, dst)

    def _step_control(self):
        '''
        Inner process control.
            0. Check output dir mainly focus on ${output}/${model_name}.
            1. Execute domain loop.
            2. Concat predict sequence data.
            3. Save to new file.
        '''
        self.checkdir(self.data_out)
        self._check_domain() 