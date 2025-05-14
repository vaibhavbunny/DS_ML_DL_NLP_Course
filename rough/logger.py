import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    filemode='w',  # 'w' for overwrite, 'a' for append
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Log messages with different severity levels.
logging.debug("This is a Debugging msg")
logging.info("This is an info msg")
logging.error("This is an error msg")
logging.warning("This is a warning msg")
logging.critical("This is a critical msg")