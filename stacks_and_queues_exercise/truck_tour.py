from collections import deque
petrol_stations_count = int(input())
stations = deque()
tank_load = 0
stops_counter = 0
full_circle = False
for i in range(petrol_stations_count):
    info_line = input().split()
    st_name = i
    petr_amount = int(info_line[0])
    dist_to_next = int(info_line[1])
    stations.append((st_name, petr_amount, dist_to_next))
while True:
    station_name = stations[0][0]
    petrol_amount = stations[0][1]
    distance_to_next = stations[0][2]
    if stops_counter == petrol_stations_count:
        full_circle = True
        break
    if petrol_amount >= distance_to_next or tank_load >= distance_to_next:
        stops_counter += 1
        tank_load += petrol_amount - distance_to_next
        stations.append(stations.popleft())
    else:
        stations.append(stations.popleft())
        stops_counter = 0
        tank_load = 0
print(station_name)

