def cross_track_distance(lat_ini, lng_ini, lat_end, lng_end, lat_other, lng_other):
    distance_ini_other = haversine(lng_ini, lng_other, lat_ini, lat_other)
    bearing_start_other = math.radians(bearing(lng_ini, lng_other, lat_ini, lat_other))
    bearing_start_end = math.radians(bearing(lng_ini, lng_end, lat_ini, lat_end))
    return math.asin(
        math.sin(math.radians(distance_ini_other/earth_radius)) *
        math.sin(bearing_start_other - bearing_start_end)
) * earth_radius