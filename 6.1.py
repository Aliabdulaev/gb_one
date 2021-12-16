import time
class TrafficLight:

    __traffic_light_color = "Светофор"

    def running(self):
        while True:
            print("Red")
            time.sleep(7)
            print("Yellow")
            time.sleep(2)
            print("Green")
            time.sleep(10)
            break


a = TrafficLight()
a.running()

