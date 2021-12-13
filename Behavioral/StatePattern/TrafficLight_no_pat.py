# https://www.youtube.com/watch?v=278vXJkgXoY&list=PLDV-cCQnUlIaGcUNSYWeDpHy_3RlMgFkU&index=3


class TrafficLight:
    def __init__(self):
        self.state = 'green'

    # prefer enum
    def setState(self, state:str):
        self.state = state

    def speak(self):
        if self.state == 'green':
            print('green light')
        elif self.state == 'red':
            print('red light')

    def wait(self):
        print('wait... the light changed')
        if self.state == 'green':
            self.state = 'red'
        elif self.state == 'red':
            self.state = 'green'

