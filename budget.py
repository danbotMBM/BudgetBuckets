# Module for calculating budget
from enum import Enum
from datetime import timedelta
from datetime import datetime

buckets = {}
removed_buckets = []

TF = Enum('TF', ["yearly", "monthly", "weekly"]) 

class bucket:
    # init with string name for identifier, int budget of dollars, timeframe of enum TF, datetime of creation, 
    def __init__(self, name, budget, timeframe, dt, cash=0):
        self.name = name
        self.budget = budget
        self.timeframe = timeframe
        self.end = self.assign_end(dt)
        self.start = self.assign_start(dt)
        self.cash = cash
        if self.name in buckets.keys():
            raise Exception
        buckets[self.name] = self

    # DEVNOTE: to optimize, accrue units of amount_used over iteration
    def drain_bucket(self, dt, amount_used):
        # drain the bucket of amount_used and send to table if timeframe is up
        # TODO how do I want to handle a series of transactions that are greater than the number of buckets
        # TODO how do I want recycling to occur and when?
        pass
    
    def assign_start(self, dt):
        match self.timeframe:
            case TF.yearly | TF.monthly:
                return dt.replace(day=1)
            case TF.weekly:
                return _floor_to_monday_(dt)
    
    def assign_end(self, dt):
        match self.timeframe:
            case TF.yearly:
                return dt.replace(year=dt.year+1)
            case TF.monthly:
                return (dt.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
            case TF.weekly:
                return _floor_to_monday_(dt)+timedelta(days=7)
    
def _floor_to_monday_(dt):
    days_to_monday = dt.weekday() # 0 is Monday, 1 is Tuesday, ..., 6 is Sunday
    delta = timedelta(days=days_to_monday)
    return dt - delta
    
