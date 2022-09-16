"""
Wrapper objects class Sessions to mesh the
data science with the web api
"""

# Imports
import pandas as pd

# Local Imports
from src.widgets.derive import slip_angle
from src.widgets.interpret import get_gps


##################
# Sessions Class #
##################

class Session:
    def __init__(self, 
                 name: str
                 ) -> None:
        # Class properties initialised at init
        self.name = name
        # TODO: Add datetime property
        
        # Class properties to be initialised at a later time
        self._df = None
        
    @property
    def df(self):
        if self.df == None:
            raise ValueError('No session data has been imported into the session')
        return self._df 
        
    def read_csv(self, 
                 path: str, 
                 units_row: int = None, 
                 header: int = 0
                 ) -> None:
        # Read the csv and cut the header
        df = pd.read_csv(path, header=header)
        
        # Remove the units row for now
        if units_row:
            df.drop(units_row, inplace=True)
        
        self.df = df
        
    def derive_channel(self,
                       channel: str
                       ) -> None:
        match channel:
            case 'Slip Angle':
                column = slip_angle(self.df)
            case _:
                raise ValueError(f'{channel} isn\'t a valid derived chanel')
        
        self.df[channel] = column            
                
    def get_gps(self,
                time: float
                ) -> list:
        """Gets GPS Coords of the car at a given time

        Args:
            time (float): The time

        Returns:
            list: [x,y,z]
        """
        return get_gps(self.df, time)
    
    
