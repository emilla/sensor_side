from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo=11, trigger=7)

#function to get the distance in cm and time it was taken as a JSON string
def get_distance():
    distance = sensor.distance * 100
    time = sensor.timestamp
    JSON = "distance:{}, time:{}}".format(distance, time)
    return JSON

