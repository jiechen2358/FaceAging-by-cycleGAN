#! /usr/bin/env python
# coding: utf-8

"""
Used to convert IMDb metadata in .mat format to .pickle format

Modified from https://gist.github.com/messefor/e2ee5fe1c18a040c90bbf91f2ee279e3

Data source: IMDB-WIKI – 500k+ face images with age and gender labels
- https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/
"""

from datetime import datetime, timedelta
import numpy as np
import scipy
from scipy.io import loadmat
import pandas as pd


def matlab_datenum2dt(matlab_datenum):
    matlab_datenum = matlab_datenum if matlab_datenum > 700000 else 700000
    return datetime.fromordinal(int(matlab_datenum) - 366) + timedelta(days=int(matlab_datenum % 1))


def main():

    path_save = '/Users/yu/Dropbox/CS230_Project/Data_Processing/imdb.pkl'
    path_mat = '/Users/yu/Dropbox/CS230_Project/Data_Processing/imdb.mat'
    mat = loadmat(path_mat)

    print(mat['__header__'])
    print(mat['__version__'])

    # Extract values
    dt = mat['imdb'][0, 0]

    # Check for columns
    print('columns:\n', dt.dtype.names)

    # Extract values with simple format
    keys_s = ('gender', 'dob', 'photo_taken',
              'face_score', 'second_face_score')
    values = {k: dt[k].squeeze() for k in keys_s}

    # Extract values with nested format
    keys_n = ('full_path', 'name')
    for k in keys_n:
        values[k] = np.array(['' if not x else x[0] for x in dt[k][0]])

    # Convert face location to DataFrame
    # img(face_location(2):face_location(4),face_location(1):face_location(3),:))
    values['face_location'] = [tuple(x[0].tolist()) for x in dt['face_location'].squeeze()]

    # Check all values extracted have same length
    set_nrows = {len(v) for _, v in values.items()}
    assert len(set_nrows) == 1

    df_values = pd.DataFrame(values)

    # Convert matlab datenum to datetime
    df_values['dob'] = df_values['dob'].apply(matlab_datenum2dt)

    # Calc ages when photo taken
    df_values['photo_taken_age'] = df_values.apply(lambda x: x['photo_taken'] - x['dob'].year, axis=1)

    # Concat all together and save
    # Do not use csv format to work around tuple to be string
    df_values.to_pickle(path_save)

if __name__ == '__main__':
    main()
