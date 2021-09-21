from collections import deque


def time_to_seconds(time: str):
    """time format is hh:mm:ss"""
    time = time.split(':')
    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2])
    hours *= 60 * 60 # hours to seconds
    minutes *= 60 # minutes to seconds
    total_time_seconds = hours + minutes + seconds
    return total_time_seconds


def seconds_to_time(seconds: int):
    days = seconds // (24 * 60 * 60)
    hours = seconds // (60 * 60)
    minutes = seconds % (60 * 60) // 60
    seconds = seconds % (60 * 60) % 60
    if hours >= 24:
        hours //= days * 24
    return f'[{hours:02d}:{minutes:02d}:{seconds:02d}]'


robots_queue = deque()
products_queue = deque()

robots_info = input().split(';')
for robot in robots_info:
    robot_specs = robot.split('-')
    robot_name = robot_specs[0]
    processing_time = int(robot_specs[1])
    start_time_for_processing = 0
    robots_queue.append([robot_name, processing_time, start_time_for_processing])

time = time_to_seconds(input())  # starting time in seconds

while True:
    product = input()
    if product == 'End':
        break
    products_queue.append(product)

while products_queue:  # while there are products to be processed
    current_product = products_queue[0]
    time += 1

    for r in range(len(robots_queue)):
        current_robot = robots_queue[0][0]
        current_processing_time = robots_queue[0][1]
        current_start_time_for_processing = robots_queue[0][2]

        if current_start_time_for_processing + current_processing_time <= time:
            robots_queue[0][2] = time  # current starting time is updated
            print(f'{current_robot} - {current_product} {seconds_to_time(robots_queue[0][2])}')
            products_queue.popleft()  # product is removed from the deque
            robots_queue.append(robots_queue.popleft())  # robot goes to end of line
            break
        robots_queue.append(robots_queue.popleft())  # robot goes to end of line
        if r == len(robots_queue) - 1:  # no robots available
            products_queue.append(products_queue.popleft())  # product goes to end of line
