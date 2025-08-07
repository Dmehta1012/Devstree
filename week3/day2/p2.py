import time
from functools import wraps
import logging
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function '{func.__name__}' executed in {end - start:.4f}s")
        return result
    return wrapper
# @timing_decorator
# def compute(n):
#     total = sum(i * i for i in range(n))
#     return total

# compute(10_000_000)


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} returned {result}")
            return result
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}", exc_info=True)
            raise
    return wrapper
@logging_decorator
@timing_decorator
def multiply(x, y):
    return x * y

multiply(5, 6)

