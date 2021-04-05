plants_count, water_count = [int(x) for x in input().split()]
plants_coords = [int(x) for x in input().split()]
water_coords = [int(x) for x in input().split()]

radius = 0
plant_ind = 0
water_ind = 0

while not (plant_ind == plants_count and water_ind == water_count - 1):
    if water_ind == water_count - 1:
        if water_coords[water_ind] >= plants_coords[plant_ind]:
            if water_ind > 0:
                radius = max(min(water_coords[water_ind] -  plants_coords[plant_ind],
                                 plants_coords[plant_ind] - water_coords[water_ind] - 1), radius)

            else:
                radius = max(radius, water_coords[water_ind] - plants_coords[plant_ind])

        else:
            radius = max(radius, plants_coords[plant_ind] - water_coords[water_ind])
        plant_ind += 1
    else:
        if water_coords[water_ind] >= plants_coords[plant_ind]:
            if water_ind > 0:
                radius = max(min(water_coords[water_ind] - plants_coords[plant_ind],
                                 plants_coords[plant_ind] - water_coords[water_ind] - 1), radius)

            else:
                radius = max(radius, water_coords[water_ind] - plants_coords[plant_ind])

            if plant_ind == plants_count - 1:
                plant_ind += 1
                break
            plant_ind += 1
        else:
            water_ind += 1


print(radius)
a = 0