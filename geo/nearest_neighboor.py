def nearest_neighboors(items_1, item2, k):
    distances = []
    for item1 in items_1:
        calc_distance = haversine(item2['origin_lng'], item2['origin_lat'], item1['lng'], item1['lat'])
        distances.append(([item2, item1], calc_distance))
    distances.sort(key = operator.itemgetter(1))
return distances[:k]