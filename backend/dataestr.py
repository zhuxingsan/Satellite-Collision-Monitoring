import datetime
from typing import Union

def getdateform(dateform: int) -> str:
    """根据日期格式编号返回日期格式字符串"""
    date_formats = {
        -1: "%d-%b-%Y %H:%M:%S",
        0: "%d-%b-%Y %H:%M:%S",
        1: "%d-%b-%Y",
        2: "%m/%d/%y",
        3: "%b",
        4: "%m",
        5: "%m",
        6: "%m/%d",
        7: "%d",
        8: "%a",
        9: "%d",
        10: "%Y",
        11: "%y",
        12: "%b%y",
        13: "%H:%M:%S",
        14: "%I:%M:%S %p",
        15: "%H:%M",
        16: "%I:%M %p",
        17: "Q%q-%y",
        18: "Q%q",
        19: "%d/%m",
        20: "%d/%m/%y",
        21: "%b.%d,%Y %H:%M:%S",
        22: "%b.%d,%Y",
        23: "%m/%d/%Y",
        24: "%d/%m/%Y",
        25: "%y/%m/%d",
        26: "%Y/%m/%d",
        27: "Q%q-%Y",
        28: "%b%Y",
        29: "%Y-%m-%d",
        30: "%Y%m%dT%H%M%S",
        31: "%Y-%m-%d %H:%M:%S",
    }
    if dateform in date_formats:
        return date_formats[dateform]
    else:
        raise ValueError(f"Unknown date format: {dateform}")


the code is coming soon
92526
78672
97432