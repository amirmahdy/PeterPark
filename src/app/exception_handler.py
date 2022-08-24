import sys
import inspect
from app.log import Log

log = Log()


def unpredicted_exception_handler(log_type):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                _, value, traceback = sys.exc_info()
                log_str = '\nTYPE: %s \nFILE: %s \nFUNC: %s \nLINE: %s \nERRR: %s \nINPT: %s' % (log_type, inspect.getfile(
                    func), func.__name__, str(traceback.tb_next.tb_lineno), str(value), str(args) + str(kwargs))
                log(log_str)
                return log_str, 400
        return inner

    return decorator


def exception_handler(log_type, frame):
    frames = inspect.getframeinfo(frame)
    _, value, traceback = sys.exc_info()
    log('\nTYPE: %s \nFILE: %s \nFUNC: %s \nLINE: %s \nERRR: %s ' % (
        log_type,  frames.filename, frames.function, str(traceback.tb_lineno), str(value)))
