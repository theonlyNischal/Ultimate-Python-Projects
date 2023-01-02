## Logging
# - Python provides **logging** which is a very powerful logging library.
# - We normally uses **print()** function for debugging purposes.
# - We can use **logging** for that
# - Logging is thread-safe.

## Creating a simple logger in python using logging library

import logging

logging.basicConfig(filename="logs/sample.log", level=logging.INFO, filemode="w")

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened.")