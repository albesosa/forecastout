from forecastout.disaggregation_features.add_features import add_features
import pandas as pd
import numpy as np


def test_add_creator():
    df = add_features(input_df())
    assert len(df) == len(input_df())


def input_df():
    date_list = [
        "2021-01-01",
        "2021-01-02",
        "2021-01-03",
        "2021-01-04",
        "2021-01-05",
        "2021-01-06",
        "2021-01-07",
        "2021-01-08",
        "2021-01-09",
        "2021-01-10",
        "2021-01-11",
        "2021-01-12",
        "2021-01-13",
        "2021-01-14",
        "2021-01-15",
        "2021-01-16",
        "2021-01-17",
        "2021-01-18",
        "2021-01-19",
        "2021-01-20"
    ]
    value_list = [
        24345.1108,
        31643.93512,
        37702.74413,
        63790.15493,
        49700.0231,
        42981.96545,
        59259.1285,
        56119.84923,
        43468.55374,
        45174.22881,
        69707.69637,
        62419.33631,
        63633.19097,
        60598.55433,
        56480.86634,
        np.nan,
        np.nan,
        np.nan,
        np.nan,
        np.nan
        ]
    return pd.DataFrame(
        {'date': pd.to_datetime(date_list), 'value': value_list}
    )
