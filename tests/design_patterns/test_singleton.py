from src.design_patterns.singleton import Singleton

class TestSingleton:
    def test_singleton(self):
        singleton1 = Singleton()
        singleton2 = Singleton()
        assert singleton1 is singleton2
