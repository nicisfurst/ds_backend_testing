"""
Given data frame, interprets a numerical value
"""
import pandas as pd
import statistics as st

def get_gps(df: pd.DataFrame, time):
    # Get coordinates of car at a time
    specified_row = df.loc[df['Time'] == time]
    coords = specified_row[["Car Coord X", "Car Coord Y", "Car Coord Z"]]

    coord_list = []
    for (colName, colData) in coords.iteritems():
        coord_list.append(colData)
    return coord_list


def get_accel(df: pd.DataFrame, time):
    # Get Accel at a time
    specified_row = df.loc[df['Time'] == time]
    accels = specified_row[["CG Accel Lateral", "CG Accel Longitudinal", "CG Accel Vertical"]]

    accel_list = []
    for (colName, colData) in accels.iteritems():
        accel_list.append(colData)
    return accel_list


def get_tireP(df: pd.DataFrame, time):
    # Get Tire Pressure at a time
    specified_row = df.loc[df['Time'] == time]
    pressures = specified_row[["Tire Pressure FL", "Tire Pressure FR", 
        "Tire Pressure RL", "Tire Pressure RR"]]

    tireP_list = []
    for (colName, colData) in pressures.iteritems():
        tireP_list.append(colData)
    return tireP_list


def get_tireT(df: pd.DataFrame, time):
    # Get Tire temps at a time
    specified_row = df.loc[df['Time'] == time]
    temps = specified_row[["Tire Temp Middle FL", "Tire Temp Middle FR", 
        "Tire Temp Middle RL", "Tire Temp Middle RR"]]

    tireT_list = []
    for (colName, colData) in temps.iteritems():
        tireT_list.append(colData)
    return tireT_list

def get_max_all(df: pd.DataFrame):
    maxes = []
    for (colName, colData) in df.iteritems():
        maxes.append(colData.max())
    return maxes

def get_min_all(df: pd.DataFrame):
    mins = []
    for (colName, colData) in df.iteritems():
        mins.append(colData.min())
    return mins

def get_mean_all(df: pd.DataFrame):
    averages = []
    for (colName, colData) in df.iteritems():
        averages.append(st.mean(colData))
    return averages







