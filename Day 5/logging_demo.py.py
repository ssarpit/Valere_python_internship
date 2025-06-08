from logging import *
basicConfig(level=DEBUG, filename='app.log', filemode='w',
            format='{asctime}-{levelname}- {message}-{process}-{lineno}', style="{")
debug("This is a debug message")
info("this is required information")
warning("warning occur")
error("error due to this log event")
critical("server error ")
