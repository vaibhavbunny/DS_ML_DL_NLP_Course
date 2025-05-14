from logger import logging 

def add(a,b):
    logging.DEBUG("Addition is taking place")
    return a + b

logging.DEBUG("Addition operation is getting called")
add(2,3)