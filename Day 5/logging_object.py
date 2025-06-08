import logging
logging.basicConfig(filename="app.log",filemode="w")
logger=logging.getLogger()
logger.setLevel(10)
logger.info("information is: ")
logger.debug("debugging started")
logging.Formatter("%(asctime)s")