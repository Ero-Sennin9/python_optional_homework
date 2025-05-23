import fcntl
import ctypes


# Singleton через переопределение __new__
class FirstSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass


# Проверка единственности
s1 = FirstSingleton()
s2 = FirstSingleton()
print(f"First singleton coincidence of variables: {s1 is s2}")


# Singleton через метакласс
class MetaSecondSingletone(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SecondSingletone(metaclass=MetaSecondSingletone):
    def __init__(self):
        pass


# Проверка единственности
m1 = SecondSingletone()
m2 = SecondSingletone()
print(f"Second singleton coincidence of variables: {m1 is m2}")  # True, один объект


# Способ 3: Singleton через ctypes
class ThirdSingletone:
    _shared_mem = None
    _lock_file = None

    def __new__(cls):
        if cls._shared_mem is None:
            cls._shared_mem = ctypes.cdll.LoadLibrary(None)
            cls._lock_file = open("/tmp/singleton_lock", "w")

        fcntl.flock(cls._lock_file, fcntl.LOCK_EX)
        try:
            if not hasattr(cls._shared_mem, "_singleton_instance"):
                instance = super().__new__(cls)
                instance.value = "SingletonCTypes"
                cls._shared_mem._singleton_instance = instance
            return cls._shared_mem._singleton_instance
        finally:
            fcntl.flock(cls._lock_file, fcntl.LOCK_UN)


# Проверка единственности
c1 = ThirdSingletone()
c2 = ThirdSingletone()
print(f"Third singleton coincidence of variables: {c1 is c2}")