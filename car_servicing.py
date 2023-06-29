from abc import ABC, abstractmethod

# not 100% sure... following given class diagram
class  Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

# Creates specific car types... not 100% on how this works w/ python syntax
class CarFactory:
    # car creation methods
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        # capulet + spindler
        engine = Capulet(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        tires = None
        car = Car(engine, battery, tires)
        return car

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        # willoughby + spindler
        engine = Willoughby(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        tires = None
        car = Car(engine, battery, tires)
        return car

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        # sternman + spindler
        engine = Sternman(warning_light_on)
        battery = Spindler(last_service_date, current_date)
        tires = None
        car = Car(engine, battery, tires)
        return car

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        # willoughby + nubbin
        engine = Willoughby(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        tires = None
        car = Car(engine, battery, tires)
        return car
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        # capulet + nubbin
        engine = Capulet(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        tires = None
        car = Car(engine, battery, tires)
        return car

# Car class
class Car(Serviceable, ABC):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()

# Engine parent class; 3 child classes
class Engine:
    def needs_service(self):
        pass

class Capulet(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.service_mileage = 30000

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= self.service_mileage

class Willoughby(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.service_mileage = 60000

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= self.service_mileage
    
class Sternman(Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on
    
# Battery parent class; 2 child classes
class Battery:
    def needs_service(self):
        pass

class Spindler(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_expiry = 3

    def needs_service(self):
        return self.current_date.year >= self.last_service_date.year + self.service_expiry

class Nubbin(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_expiry = 4

    def needs_service(self):
        return self.current_date.year >= self.last_service_date.year + self.service_expiry
    
# Tire parent class; 2 child classes
class Tires:
    def needs_service(self):
        pass

class Carrigan(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.max_wear = 0.9

    def needs_service(self):
        for i in self.tire_wear:
            if i >= self.max_wear:
                return True
        return False

class OctoPrime(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.max_wear = 3

    def needs_service(self):
        wear_sum = 0
        for i in self.tire_wear:
            wear_sum += i
        
        if wear_sum >= self.max_wear:
            return True

        return False