from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo=18, trigger=17)

#function to get the distance in cm and time it was taken as a JSON string
def get_distance():
    distance = sensor.distance * 100
    now  = time.time()
    JSON = '{"distance":"{}", "time":"{}"}'.format(distance, now)
    return JSON

