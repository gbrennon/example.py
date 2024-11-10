from src.design_patterns.creational.singleton import Singleton, DO_SOMETHING

class TestSingleton:
    def test_singleton_instance_is_unique(self):
        # Arrange: Create two instances of the Singleton class
        singleton1 = Singleton()
        singleton2 = Singleton()

        # Act: The action is to instance the Singleton class
        result = singleton1 is singleton2

        # Assert: The two instances are the same
        assert result, "The two instances should be the same"

    def test_singleton_do_something(self):
        # Arrange: Create an instance of the Singleton class
        singleton = Singleton()

        # Act: The action is to call the do_something method
        result = singleton.do_something()

        # Assert: The method returns the expected value
        expected = DO_SOMETHING
        assert(
            result == expected
        ), r"The method should return '{expected}'"
