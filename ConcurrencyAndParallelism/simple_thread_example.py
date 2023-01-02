import time
import logging
import threading

def get_logger():
    """A function to get a logger object.
    """
    # create logger
    logger = logging.getLogger("simple_thread_example")
    # set logger level
    logger.setLevel(logging.DEBUG)

    # create a file handler
    fh = logging.FileHandler("logs/simple_thread_example.log")
    # create a formatter and set the formatter for the handler.
    fmt = logging.Formatter("%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s")
    fh.setFormatter(fmt)
    # add the Handler to the logger
    logger.addHandler(fh)

    # return the logger
    return logger

def double_number(number, logger):
    """A function to double a number.
    """
    logger.info("Started double_number")
    time.sleep(1)
    result = number * 2
    logger.info("Finished double_number")
    return result

if __name__ == "__main__":
    start_time = time.time()
    # get a logger
    logger = get_logger()

    # thread names
    thread_names = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5"]

    for i in range(5):
        # create a thread
        t = threading.Thread(target=double_number, name=thread_names[i], args=(i, logger))
        # start the thread
        t.start()
    end_time = time.time()
    print(f"Total time: {end_time-start_time}")
