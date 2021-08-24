class Car:

    def __init__(self):
        '''
        __init__() initializes the attributes in the Car class
        arg:
        -- self

        return
        -- None
        '''
        import random

        self.__make = self.setMake() # used to set the make of the car
        self.__model = self.setModel(self.__make) # used to set the model of the car
        self.__mileage = random.randint(0, 550000 ) # random mileage from 0 to 550k in km
        self.__speed = random.randint(0, 80) # random speed from 0 to 80 in km/h

    def __repr__(self):
        '''
        __repr__() allows to present printable version of object
        arg:
        -- self

        return
        -- self.__str__() : method
        '''

        return self.__str__()

    def __str__(self):
        '''
        __str__() allows to convert object to a string
        arg:
        -- self

        return
        -- string
        '''

        return f'Current car is: {newCar.getBuild()}'

    def setMake(self):
        '''
        setMake() sets the make and year of the car
        arg:
        -- self

        return
        -- string
        '''

        import random

        make = ['Toyota', 'Honda', 'Nissan', 'GMC']
        rMake = random.randrange(len(make)) # used to randomize the make of the car
        year = str(random.randint(1990, 2021)) # used to randomize the production year of the car
        
        return year + ' ' + make[rMake]

    def setModel(self, make):
        '''
        setModel() sets the model of the car based on the make of the car
        arg:
        -- self
        -- make : string

        return
        -- model : list
        '''

        import random
        brand = make.split()[1] # used to get the make of the car

        if brand == 'Toyota':
            model = ['Supra', 'Corolla', '86', 'Sienna']
        elif brand == 'Honda':
            model = ['CR-V', 's2000', 'Civic', 'Accord']
        elif brand == 'Nissan':
            model = ['Skyline', 'Sylvia', 'GT-R', 'Pathfinder']
        else:
            model = ['Yukon', 'Acadia', 'Sierra', 'Canyon']

        rModel = random.randrange(len(model))

        return model[rModel]

    def getBuild(self):
        '''
        getBuild() used for displaying the year, make, and model of the car all at once
        arg:
        -- self

        return
        -- string
        '''

        return self.__make + ' ' + self.__model
    
    def accelerate(self):
        '''
        accelerate() called in order to accelerate the car
        arg:
        -- self

        return
        -- self.__speed : int
        '''

        self.__speed += 15 # increases the speed by 15 km/h
        return self.__speed
    
    def brake(self):
        '''
        brake() called in order to slow down the car
        arg:
        -- self

        return
        -- self.__speed : int
        '''

        self.__speed -= 10 # decreases the speed by 10 km/h
        return self.__speed

    def engineLife(self):
        '''
        engineLife() called in order to display the engines health based on mileage
        arg:
        -- self

        return
        -- string
        '''

        print('Car mileage is:', self.__mileage, 'km')

        if self.__mileage <= 50000:
            return('Engine health is in mint condition!')
        elif self.__mileage > 50000 and self.__mileage <= 75000:
            return('Engine health is in good condition!')
        elif self.__mileage > 75000 and self.__mileage <= 150000:
            return('Engine health is in fairly decent condition.')
        elif self.__mileage > 150000 and self.__mileage <= 300000:
            return('Engine health is in poor condition...')
        elif self.__mileage > 300000:
            return('Engine is currently running on life support...')
        
    def speedometer(self):
        '''
        speedometer() called in order to display the current speed of the car
        arg:
        -- self

        return
        -- self.__speed : int
        '''
        return self.__speed

    def headlights(self, isDay):
        '''
        headlights() used for turning the headlights of the car on and off based on time of day
        arg:
        -- self
        -- isDay : Boolean

        return
        -- string
        '''
        # checks if it is day or not
        if isDay == False:
            return 'ON'
        else:
            return 'OFF'
        
import random

newCar = Car()

print(newCar)

print()
print('------------------------------------')
print('Current speed is:', newCar.speedometer(), 'km/h')
print('Accelerating to:', newCar.accelerate(), 'km/h')
print('Decelerating to:', newCar.brake(), 'km/h')
print()
print(newCar.engineLife())
print()
print('Current headlight status:', newCar.headlights(isDay = random.choice([True, False])))
print('------------------------------------')
