import logging
import otherModule

def main():
    """
    The main entry point of the application.
    """
    logging.basicConfig(filename="logs/mySnake.log", level=logging.INFO)
    logging.info("Program Started.")
    result = otherModule.add(7, 8)
    logging.info("Done!")

if __name__ == "__main__":
    main()