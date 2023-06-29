import unittest
from datetime import datetime

from car_servicing import Capulet
from car_servicing import Willoughby
from car_servicing import Sternman
from car_servicing import Spindler
from car_servicing import Nubbin
from car_servicing import Carrigan
from car_servicing import OctoPrime

class TestCapulet(unittest.TestCase):
    def test_engine_needs_no_service(self):
        last_service_mileage = 30100
        current_mileage = 51000

        engine = Capulet(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
    
    def test_engine_needs_service(self):
        last_service_mileage = 60001
        current_mileage = 90050

        engine = Capulet(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_needs_no_service(self):
        last_service_mileage = 60001
        current_mileage = 80500

        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
    
    def test_engine_needs_service(self):
        last_service_mileage = 60100
        current_mileage = 121000

        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_needs_no_service(self):
        warning_light_on = False

        engine = Sternman(warning_light_on)
        self.assertFalse(engine.needs_service())
    
    def test_engine_needs_service(self):
        warning_light_on = True

        engine = Sternman(warning_light_on)
        self.assertTrue(engine.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_needs_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = Spindler(last_service_date, today)
        self.assertFalse(battery.needs_service())
    
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = Spindler(last_service_date, today)
        self.assertTrue(battery.needs_service())

class TestNubbin(unittest.TestCase):
    def test_battery_needs_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery = Nubbin(last_service_date, today)
        self.assertFalse(battery.needs_service())
    
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = Nubbin(last_service_date, today)
        self.assertTrue(battery.needs_service())

class TestCarrigan(unittest.TestCase):
    def test_tires_need_no_service(self):
        tire_wear = [0.5, 0.7, 0.1, 0]

        tires = Carrigan(tire_wear)
        self.assertFalse(tires.needs_service())
    
    def test_tires_need_service(self):
        tire_wear = [0.3, 0.5, 1, 0.3]

        tires = Carrigan(tire_wear)
        self.assertTrue(tires.needs_service())

class TestOctoPrime(unittest.TestCase):
    def test_tires_need_no_service(self):
        tire_wear = [0.1, 0.7, 0.1, 1]

        tires = OctoPrime(tire_wear)
        self.assertFalse(tires.needs_service())
    
    def test_tires_need_service(self):
        tire_wear = [0.9, 0.5, 1, 0.7]

        tires = OctoPrime(tire_wear)
        self.assertTrue(tires.needs_service())