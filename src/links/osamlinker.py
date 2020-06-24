# -*- encoding: utf-8 -*-
'''
@Filename    : osamlinker.py
@Datetime    : 2020/06/23 17:44:06
@Author      : Joe-Bu
@version     : 1.0
'''

import os
import sys
from datetime import datetime, timedelta

from links.baselink import baseLink


class osamLink(baseLink):
    '''
    OSAM Emission Data Pre_processing Class.
        Function:
            Generate soft link between src base data and dst data.
    '''
    def __init__(self, name: str, this_time: datetime, cfg: dict, in_path: str, out_path: str):
        super().__init__(name=name, this_time=this_time)
        # base cfg
        # TODO: dict loop
        self.base_year = cfg.get('base_year')
        self.base_day = cfg.get('base_day')
        self.domains = cfg.get('domains')
        self.dt_format = cfg.get('dt_format')
        self.pred_seq = cfg.get('pred_seq')
        self.source = cfg.get('source')
        # data dir
        self.data_in = os.path.join(in_path, self.name)
        self.data_out = os.path.join(out_path, self.name)

    def _check_source(self):
        '''
            Source Loop.
        '''
        assert isinstance(self.source, list)

        for source in self.source:
            self._check_domain(source)        

    def _check_domain(self, source: str):
        '''
            Domain Loop.
        '''
        assert isinstance(self.domains, list) and len(self.domains)>=1

        for domain in self.domains:
            self._check_time(domain, source)

    def _check_time(self, domain: int, source: str):
        '''
            Predict Sequence Loop.
        '''
        # TODO: move start-time forward n hours.
        start = self.this_time
        end = start + timedelta(hours=self.pred_seq)

        while start <= end:
            src_file = 'emis.{0}.{1}{2}{3}{4}.d{5}'.format(
                source,
                self.base_year, 
                start.strftime("%m"), 
                self.base_day, 
                start.strftime("%H"), 
                domain)
            dst_file = 'emis.{0}.{1}.d{2}'.format(
                source,
                start.strftime(self.dt_format), 
                domain)
            src = os.path.join(self.data_in, src_file)
            dst = os.path.join(self.data_out, dst_file)

            # ln -sf src dst
            self.gen_sflink(src, dst)
            start += timedelta(hours=1)

    def _step_control(self):
        '''
        Inner process control.
        '''
        self.checkdir(self.data_out)
        self._check_source()