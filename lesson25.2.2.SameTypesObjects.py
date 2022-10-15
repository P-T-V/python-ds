class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    resolution = 'WQHD'
    frequency = 60


class Headphone:
    name = 'Sony'
    sensitivity = 108
    microphone = True


monitor_1 = Monitor()
monitor_2 = Monitor()
monitor_3 = Monitor()
monitor_4 = Monitor()
monitor_2.frequency = 144
monitor_3.frequency = 70
headphone_1 = Headphone()
headphone_2 = Headphone()
headphone_3 = Headphone()
headphone_1.microphone = False
print(monitor_1.name, monitor_1.matrix, monitor_1.resolution, monitor_1.frequency)
print(monitor_2.name, monitor_2.matrix, monitor_2.resolution, monitor_2.frequency)
print(monitor_3.name, monitor_3.matrix, monitor_3.resolution, monitor_3.frequency)
print(monitor_4.name, monitor_4.matrix, monitor_4.resolution, monitor_4.frequency)
print(headphone_1.name, headphone_1.sensitivity, headphone_1.microphone)
print(headphone_2.name, headphone_2.sensitivity, headphone_2.microphone)
print(headphone_3.name, headphone_3.sensitivity, headphone_3.microphone)
