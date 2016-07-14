# '__' means it is private
class Animal( object ):
    __name = None
    __height = 0
    __weight = 0
    __sound = None
    
    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
    
    def get_type(self):
        print "Animal"
    
    def to_string(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(
                                                                    self.__name,
                                                                    self.__height,
                                                                    self.__weight,
                                                                    self.__sound
                                                                    )
    #getters and setters
    
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_height(self, height):
        self.__height = height
        
    def get_height(self):
        return self.__height
    
    def set_weight(self, weight):
        self.__weight = weight
        
    def get_weight(self):
        return self.__weight
    
    def set_sound(self, sound):
        self.__sound = sound
        
    def get_sound(self):
        return self.__sound


    
cat = Animal('Mel',33,10,"Miau")                                

print cat.to_string()
cat.get_type()

class Dog(Animal):
    __owner = ""
    
    def __init__(self,name,height,weight,sound,owner):
        self.__owner = owner
        super(Dog, self).__init__(name,height,weight,sound)
    
    def to_string(self):
        return "{} is {} cm tall and {} kilograms and says {} and owner is {}".format(
                                                                    super(Dog, self).get_name(),
                                                                    super(Dog, self).get_height(),
                                                                    super(Dog, self).get_weight(),
                                                                    super(Dog, self).get_sound(),
                                                                    self.__owner
                                                                    )
    def set_owner(self, owner):
        self.__owner = owner
        
    def get_owner(self):
        return self.__owner 
    
    #override
    def get_type(self):
        print "Dog"

    #overloading
    def multiple_sounds(self, how_many = None):
        if how_many is None:
            print self.get_sound()
        else:
            print (self.get_sound()+" ") * how_many

dog = Dog("Scooby", 53, 27, "HOU", "Rayssa")

print dog.to_string()
dog.get_type()

dog.multiple_sounds()
dog.multiple_sounds(3)


class AnimalTesting:
    def get_type(self,animal):
        animal.get_type()

testAnimals = AnimalTesting()
testAnimals.get_type(cat)
testAnimals.get_type(dog)