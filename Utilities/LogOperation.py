import logging

from Utilities import Utility

logFolder=Utility.projectDirectory()+"\\Report\\Log\\"

def logInfo(info):
    logging.basicConfig(filename=logFolder+"log.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)
    log = logging.getLogger()
    log.info(info)


def logError(error):
    logging.basicConfig(filename=logFolder+"log.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.ERROR)
    log = logging.getLogger()
    log.error(error)