import logging

def add(x,y):
    """Add Function"""
    logging.info("added {} and {} to get {}.".format(x, y, x+y))
    return x+y