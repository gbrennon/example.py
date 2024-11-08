from src.design_patterns.creational.singleton import Singleton

class TestSingleton:
    def test_singleton(self):
        value = 'value'
        singleton1 = Singleton(value,)
        singleton2 = Singleton(value,)
        assert singleton1 is singleton2
