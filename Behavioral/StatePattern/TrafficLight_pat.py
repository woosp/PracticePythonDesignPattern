# https://www.youtube.com/watch?v=278vXJkgXoY&list=PLDV-cCQnUlIaGcUNSYWeDpHy_3RlMgFkU&index=3


class TrafficLight:
    def __init__(self):
        self.state = GreenLight()

    def setState(self, state:str):
        self.state = state

    def speak(self):
        # call speak
        self.state.speak()

    def wait(self):
        # call wait
        self.state.wait(self)

# State interface
class State:
    def speak(self):
        pass

    # We use TrafficLight object here to pass state info to each other
    def wait(self, traffic_light: TrafficLight):
        pass

# Child class of state
#   Each child needs to know the existence of other State (e.g. RedLight)
class GreenLight(State):
    def speak(self):
        print('green light')

    def wait(self, traffic_light: TrafficLight):
        print('wait... the light changed')
        traffic_light.setState(RedLight())

# Child class of state
class RedLight(State):
    def speak(self):
        print('red light')

    def wait(self, traffic_light: TrafficLight):
        print('wait... the light changed')
        traffic_light.setState(GreenLight())






