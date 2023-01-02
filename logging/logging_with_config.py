import logging
import logging.config
import otherModule2

def main():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('exampleApp')

    logger.info("Program Started.")
    result = otherModule2.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()