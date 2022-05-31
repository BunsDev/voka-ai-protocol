import logging

from exceptions.ExceptionEntity import ExceptionEntity, LackParamsException, NotFoundException

logger = logging.getLogger(__name__)

# exception handler entry point
def exceptionHandler(e: Exception) -> ExceptionEntity:
    code: int = 500
    msg = e.args

    if type(e) == KeyError:
        code = 400
    elif type(e) == NameError:
        code = 400
    elif type(e) == LackParamsException:
        code = 400
    elif type(e) == NotFoundException:
        code = 400
    else:
        code: int = 500

    logger.error("{} msg: {}".format(type(e), msg))
    return ExceptionEntity(code, msg)
    