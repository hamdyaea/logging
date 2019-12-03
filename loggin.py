#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein

import logging

logging.basicConfig(
    filename="example.log",
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)  # log to a file


def logger():
    logging.debug("This message should go to the log file")
    logging.critical("I am a critial login")
    logging.info("So should this")
    logging.warning("And this, too")
    logging.error("I am an error message logged")
    myvar = "Je suis une variable"
    myvar1 = "Je suis une autre variable !"
    logging.info(
        " Variable : %s" % myvar + str(" Variable 2 : %s" % myvar1)
    )  # log a variable


logger()
