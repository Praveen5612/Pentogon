class Metro:
    def __init__(self):
        self.color= 'Yellow'

    def move(self):
        print('Metro is moving')
    
    @staticmethod
    def stop():
        print('Metro is stopping')
    
    @classmethod
    def carry_passengers(cls):
        print('Metro is carrying passengers')
    
m1=Metro()
m1.move()   
Metro.stop()
Metro.carry_passengers()