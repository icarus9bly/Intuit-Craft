import logging
import logging.config
from functools import wraps
import time
import yaml
from django.conf import settings

# initiate logger

with open(str(settings.BASE_DIR) + '/snl-logger.yaml') as log_file:
    log_dict = yaml.safe_load(log_file)
    filename = str(settings.BASE_DIR) + '/logs/snl.log'
    log_dict['handlers']['log_file_handler']['filename'] = filename
logging.config.dictConfig(log_dict)
mana_logger = logging.getLogger('naLogger')


# Time logger
def na_timer(orig_func):
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        if result:
            for key,value in result.items():
                logger.error("%s %r" %(key,value))
        t2 = time.time() - t1
        logger.info("[END] %s completed in %f secs" %(orig_func.__name__, t2))
        return result
    return wrapper

# Name logger
def na_logger(orig_func):
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("[BEGIN] Execution of %s" %(orig_func.__name__)) 
        return orig_func(*args, **kwargs)
    return wrapper