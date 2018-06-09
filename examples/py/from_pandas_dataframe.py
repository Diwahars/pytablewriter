#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from textwrap import dedent

import pytablewriter
import six

import pandas as pd


csv_data = six.StringIO(dedent("""\
    "i","f","c","if","ifc","bool","inf","nan","mix_num","time"
    1,1.10,"aa",1.0,"1",True,Infinity,NaN,1,"2017-01-01 00:00:00+09:00"
    2,2.20,"bbb",2.2,"2.2",False,Infinity,NaN,Infinity,"2017-01-02 03:04:05+09:00"
    3,3.33,"cccc",-3.0,"ccc",True,Infinity,NaN,NaN,"2017-01-01 00:00:00+09:00"
    """))
df = pd.read_csv(csv_data, sep=',')

writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()
