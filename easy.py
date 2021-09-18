import time
import datetime
import re
from typing import Pattern

# 1
def day_diff(release_date, code_complete_day):

    releaseDate = datetime.datetime.strptime(release_date, '%d/%m/%Y')

    completeDay = datetime.datetime.strptime(code_complete_day, '%Y-%d-%m')
    cal_day = releaseDate - completeDay  
    
    return cal_day.days

# 2
def alpha_num(sentence):

    pattern = "\w+\d|\d+\w"
    reg = re.findall(pattern, sentence)
    return reg

