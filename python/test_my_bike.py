import unittest
from my_bike import Bike

class TestAutomaticBike(unittest.TestCase):
    def test_if_the_bike_will_turn_on(self):
        my_bike = Bike()
        my_bike.start()
        self.assertEqual("Power on", my_bike.power())  # add assertion here

    def test_if_the_bike_will_turn_off(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.stop()
        my_bike.power()
        self.assertEqual("Power off", my_bike.power())

    def test_if_the_gear_increases_while_the_bike_is_on(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        self.assertEqual(1, my_bike.check_gear())

    def test_if_the_gear_increases_while_the_bike_is_off(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.stop()
        my_bike.set_gear()

        self.assertTrue(my_bike.power())
        self.assertEqual(0, my_bike.check_gear())

    def test_if_acceleration_function_increases_once_not_Twice(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        my_bike.set_gear()
        my_bike.set_gear()
        my_bike.accelerate()

        self.assertEqual(1, my_bike.check_acceleration())
        self.assertEqual(1, my_bike.check_gear())
    def test_for_multiple_accelerations(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        my_bike.accelerate()
        my_bike.accelerate()
        my_bike.accelerate()

        self.assertEqual(3, my_bike.check_acceleration())

    def test_if_the_bike_will_accelerate_when_the_bike_is_off(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        my_bike.stop()
        my_bike.accelerate()
        my_bike.accelerate()
        my_bike.accelerate()

        self.assertEqual(0, my_bike.check_acceleration())

    def test_if_the_bike_automatically_changes_gear_when_the_acceleration_exceed_20(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(21):
            my_bike.accelerate()
        self.assertEqual(2, my_bike.check_gear())
        self.assertEqual(21, my_bike.check_acceleration())

    def test_if_the_bike_automatically_changes_gear_when_the_acceleration_exceeds_30(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(26):
            my_bike.accelerate()
        self.assertEqual(31, my_bike.check_acceleration())
        self.assertEqual(3, my_bike.check_gear())

    def test_if_the_bike_automatically_changes_gear_when_the_acceleration_exceeds_40(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(30):
            my_bike.accelerate()
        self.assertEqual(43, my_bike.check_acceleration())
        self.assertEqual(4, my_bike.check_gear())

    def test_if_the_bike_remains_at_gear_4_when_the_acceleration_exceeds_50(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(50):
            my_bike.accelerate()
        self.assertEqual(123, my_bike.check_acceleration())
        self.assertEqual(4, my_bike.check_gear())

    def test_if_the_acceleration_wil_stop_adding_when_it_exceeds_120(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(2334):
            my_bike.accelerate()
        self.assertEqual(123, my_bike.check_acceleration())
        self.assertEqual(4, my_bike.check_gear())


    def test_if(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(120):
            my_bike.accelerate()
        self.assertEqual(123, my_bike.check_acceleration())
        self.assertEqual(4, my_bike.check_gear())

    def test_for_single_decelerations(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(2):
            my_bike.accelerate()
        my_bike.decelerate()
        self.assertEqual(1, my_bike.check_acceleration())
        self.assertEqual(1, my_bike.check_gear())

    def test_for_multiple_decelerations(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(5):
            my_bike.accelerate()
        for num in range(4):
             my_bike.decelerate()
        self.assertEqual(1, my_bike.check_acceleration())
        self.assertEqual(1, my_bike.check_gear())


    def test_the_gear_level_when_deceleration_is_less_than_50(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(50):
            my_bike.accelerate()
        for _ in range(20):
            my_bike.decelerate()
        self.assertEqual(43, my_bike.check_acceleration())
        self.assertEqual(4, my_bike.check_gear())

    def test_the_gear_level_when_deceleration_is_less_than_40(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(50):
            my_bike.accelerate()
        for _ in range(23):
            my_bike.decelerate()
        self.assertEqual(33, my_bike.check_acceleration())
        self.assertEqual(3, my_bike.check_gear())

    def test_the_gear_level_when_acceleration_is_lesser_than_30(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(50):
            my_bike.accelerate()
        for _ in range(26):
            my_bike.decelerate()
        self.assertEqual(26, my_bike.check_acceleration())
        self.assertEqual(2, my_bike.check_gear())

    def test_the_gear_level_when_acceleration_is_lesser_than_20(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        for _ in range(50):
            my_bike.accelerate()
        for _ in range(30):
            my_bike.decelerate()
        self.assertEqual(19, my_bike.check_acceleration())
        self.assertEqual(1, my_bike.check_gear())


    def test_the_gear_level_when_acceleration_is_0(self):
        my_bike = Bike()
        my_bike.start()
        my_bike.set_gear()
        my_bike.accelerate()
        my_bike.decelerate()
        self.assertEqual(0, my_bike.check_acceleration())
        self.assertEqual(0, my_bike.check_gear())

if __name__ == '__main__':
    unittest.main()
