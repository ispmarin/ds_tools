def bearing(lon1, lon2, lat1, lat2):
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    return (math.degrees(
        math.atan2(
            math.sin(lon2 - lon1) * math.cos(lat2),
            math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)

        )
    ) + 360) % 360