#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def read_logbook(ifile, startdate=None, enddate=None):
    import pandas

    df = pandas.read_csv(ifile, sep=' *; *')

    pandas.to_datetime(df['date'])
    if startdate is not None and enddate is not None:
        df = df.loc[(df['date'] > startdate) &
                    (df['date'] <= enddate)]
    if(df.empty):
        distance = 0
        last_date = enddate
    else:
        distance = df['meter'].sum(axis=0)
        last_date = df['date'].values[-1]

    return distance, last_date
