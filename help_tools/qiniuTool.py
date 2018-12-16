import os
from _datetime import datetime

def getFileUrl(instance, filename):
    unique_name = datetime.now().strftime('%Y%m%d%H%M%S') + filename
    return unique_name