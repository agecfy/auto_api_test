import os

ENV = os.getenv("TEST_ENV", "dev")

CONFIG = {
    "dev": {
        "base_url": "https://jsonplaceholder.typicode.com",
    },
    "sit": {
        "base_url": "https://jsonplaceholder.typicode.com",
    }
}

def get_base_url():
    return CONFIG[ENV]["base_url"]
