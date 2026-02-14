import time
import random

def retry_request(func, retries=3, base_delay=1):
    """
    Retries a function call with exponential backoff.
    """
    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as e:
            if attempt == retries:
                raise e
            sleep_time = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 0.5)
            print(f"⚠️ Retry {attempt}/{retries} failed. Retrying in {sleep_time:.2f}s...")
            time.sleep(sleep_time)
