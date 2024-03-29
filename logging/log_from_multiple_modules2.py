# WAP to build a logger that can log from multiple modules
# and also log to a file.

import logging
import otherModule2

def main():
    """
    The main entry point of the application."""
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("logs/new_snake.log")
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = otherModule2.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()