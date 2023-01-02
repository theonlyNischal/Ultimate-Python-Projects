import logging

module_logger = logging.getLogger("exampleApp.otherModule2")

def add(x,y):
    logger = logging.getLogger("exampleApp.otherModule2.add")
    logger.info("added {} and {} to get {}".format(x, y, x+y))
    return x+y