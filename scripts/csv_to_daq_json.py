"""
Converts CSV files exported from Motec into json files in the same format
used by DAQ.
"""

import pandas as pd
from sys import argv
from json import dump
from pathlib import Path

# channels to keep
CHANNELS = [
    'Time',
    'Distance',
    'Brake Pos',
    'CG Accel Lateral',
    'CG Accel Longitudinal',
    'CG Accel Vertical',
    'Ground Speed',
    'Steering Angle',
    'Throttle Pos'
    ]


def main():
    units, df = get_cleaned_csv()
    js = make_json(units, df)
    save_json(js)
    # save_json({'apple': ['orange', 'pear']})
    
    
def get_cleaned_csv():
    if len(argv) <= 1:
        raise Exception('No file was passed to argv')
    # Get df
    df = pd.read_csv(argv[1], header=12).loc[:, CHANNELS]
    units = df.loc[0]
    df = df.loc[1:]
    # print(df.head())
    return units, df


def make_json(units: pd.Series, df: pd.DataFrame):
    js = {'inputs': [], 'data': []}
    ids = {}
    
    # Add inputs
    i = 0
    for channel, unit in units.items():
        js['inputs'].append({
            'channelName': channel,
            'channelNumber': i,
            'units': unit
        })
        ids[channel] = i
        i += 1
    
    # Add data points
    for _, data_point in df.iterrows():
        time = data_point['Time']
        data_point.drop('Time', inplace=True)
        for channel, value in data_point.items():
            js['data'].append({
                'channel': ids[channel],
                'time': time,
                'value': value
            })
 
    return js


def save_json(js: str):
    path = Path(argv[1])
    
    name = path.name
    new_path = path.parent.parent / 'json' 
    new_path.mkdir(exist_ok=True)
    full_fpath = (new_path / name).with_suffix('.json')
    
    # Save the json
    with open(full_fpath, 'w') as f:
        dump(js, f, indent=2)


if __name__ == '__main__':
    main()
