from os import listdir
import os.path as p
import csv
from datetime import date, timedelta

from utils import utils

ACCOUNTING_TYPES = {'asset': 1,
                    'liability': -1}


class AccountBalances:
    """
    Class to load/store/manipulate account-balance data
    """
    BASE_PATH = 'account_balances'
    ID_COL = 'account_id'
    TYPE_COL = 'accounting_type'
    DATE_COL = 'balance_date'
    BALANCE_COL = 'balance'
    DATE_FORMAT = '%m/%d/%Y'

    def __init__(self):
        self.accounts = {}
        self.events = []
        path = p.join(p.dirname( __file__ ), self.BASE_PATH)
        for filename in listdir(path):
            full_name = p.join(path,filename)
            if not p.isfile(full_name):
                continue

            with open(full_name) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    account_id = row[self.ID_COL]
                    account_type = row[self.TYPE_COL]
                    self.accounts[account_id] = account_type
                    self.events.append(
                        (utils.get_date(row[self.DATE_COL],self.DATE_FORMAT),account_id,float(row[self.BALANCE_COL])))
        self.events.sort()

    def net_worths(self, start_date=date.today(), end_date=date.today()):
        """
        Takes in a date range and outputs a list of tuples (date,net worth) for all dates in that range (inclusive)
        """
        output = []
        balances = {}
        output_date = start_date

        for bal_date,acct,bal in self.events:
            prev_net_worth = self.__net_worth(balances)
            while output_date < bal_date and output_date <= end_date:
                output.append((output_date,prev_net_worth))
                output_date += timedelta(1)

            balances[acct] = bal

            if output_date > end_date:
                break
        else:
            final_net_worth = self.__net_worth(balances)
            while output_date <= end_date:
                output.append((output_date,final_net_worth))
                output_date += timedelta(1)
        return output

    def __net_worth(self,balances):
        return sum([ACCOUNTING_TYPES[self.accounts[account]]*balance for account,balance in balances.iteritems()])
