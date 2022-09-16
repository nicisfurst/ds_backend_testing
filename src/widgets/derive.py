"""
Functions that are passed a pd data frame
Does stuff and returns a pd series    
"""

import pandas as pd

def slip_angle_front(df: pd.DataFrame):
    cornering_stiffness = 100   # Find which value this actually is from the original dataframe 

    df['Slip Angle Front'] = df['CG Accel Lateral'].astype(float) * df['CG Accel Longitudinal'].astype(float)
    return df['Slip Angle Front']

def slip_angle_rear(df: pd.DataFrame):
    cornering_stiffness = 100   # Find which value this actually is from the original dataframe 

    df['Slip Angle Rear'] = df['CG Accel Lateral'].astype(float) * df['CG Accel Longitudinal'].astype(float)
    return df['Slip Angle Rear']

