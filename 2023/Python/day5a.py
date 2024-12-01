with open("input5.txt", 'r') as fp:
    data = fp.read()
    
lines = data.split("\n")
seeds = list(map(int, lines[0].strip("seeds :").split()))

print(seeds)

def get_map(map_data):
    out_map = {'source': [], 'destination': []}
    lines = map_data.split("\n")
    name = lines[0]
    ranges = lines[1:]
    for r in ranges:
        destination_start, source_start, count = r.split()
        destination_start, source_start, count = int(destination_start), int(source_start), int(count)

        # for i, j in zip(range(source_start, source_start+count), (range(destination_start, destination_start+count))):
        #     out_map[i] = j
        out_map['source'].append(range(source_start, source_start+count))
        out_map['destination'].append(range(destination_start, destination_start+count))
        # print(r, out_map)
        #print(destination_start, source_start, count)
    return out_map

all_maps = data.split("\n\n")

# seed_to_soil = get_map(all_maps[1])
# soil_to_fertilizer = get_map(all_maps[2])
# fertilizer_to_water = get_map(all_maps[3])
# water_to_light = get_map(all_maps[4])
# light_to_temperature = get_map(all_maps[5])
# temperature_to_humidity = get_map(all_maps[6])
# humidity_to_location = get_map(all_maps[7])
# print(humidity_to_location)

def get_value(val: int, the_map: dict):
    # print(val, the_map)
    for k in the_map['source']:
        if val in k:
            return the_map['destination'][the_map['source'].index(k)].start + (val - k.start)
        
    return val
    # if val in range(list(the_map.keys())[0], list(the_map.keys())[-1] + 1):
    #     return the_map[val - list(the_map.keys())[0]]
    # else:
    #     return val

locations = []
for s in seeds:
    #location = humidity_to_location[temperature_to_humidity[light_to_temperature[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[s]]]]]]]
    #locations.append(location)
    a = get_value(s, get_map(all_maps[1]))
    b = get_value(a, get_map(all_maps[2]))
    c = get_value(b, get_map(all_maps[3]))
    d = get_value(c, get_map(all_maps[4]))
    e = get_value(d, get_map(all_maps[5]))
    f = get_value(e, get_map(all_maps[6]))
    g = get_value(f, get_map(all_maps[7]))
    print(s, a, b, c, d, e, f, g)

    locations.append(g)

print(min(locations))