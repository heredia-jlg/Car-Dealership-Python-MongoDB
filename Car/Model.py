class Car:
    '''Car class'''
    def _init_(self, make='', model='', year='', price=''):
        "Instanciates car object"
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        '''The state can be 'None' or 'owned'  '''
        self.state = None
    
    @classmethod
    def to_dict(self):
        '''Creates and returns a dictionary representation of instance'''
        dictionary = self.__dict__
        return dictionary

    @classmethod
    def from_dict(cls, dictionary):
        '''Creates an instance of the class from a dictionary input'''
        car = Car()
        car.__dict__.update(dictionary)
        return car

    @classmethod
    def create_new(cls):
        '''Prompts user for input to create new instance of a car'''
        new_car = Car().to_dict()
        new_car['make'] = input('Enter make: ')
        new_car['model'] = input('Enter model: ')
        new_car['year'] = input('Enter year: ')
        new_car['price'] = input('Enter price: ')
        new_car['state'] = None
        return Car.from_dict(new_car)
