import unittest
from datetime import datetime

from car_servicing import Capulet
from car_servicing import Willoughby
from car_servicing import Sternman
from car_servicing import Spindler
from car_servicing import Nubbin

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
        last_service_date = today.replace(year=today.year - 2)

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
