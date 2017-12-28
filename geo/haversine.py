# Ivan Marin
# ispmarin@gmail.com

import numpy as np


def haversine(lon1, lat1, lon2, lat2):
    # Distance between two points
    # assuming that the input is in WGS84 and is equivalent
    # to SIRGAS 2000
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    a = np.sin((lat2 - lat1 )/2.)**2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1)/2.)**2
    c = 2. * np.arcsin(np.sqrt(a)) 
    km = 6367. * c
    return km

