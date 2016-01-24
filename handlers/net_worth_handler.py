from tornado import escape
from tornado.web import RequestHandler

from utils import utils
from data.dal import AccountBalances


class NetWorthHandler(RequestHandler):
    def get(self):
        try:
            query_params = self.request.arguments
            start_date = utils.get_date(query_params['from'][0])
            end_date = utils.get_date(query_params['to'][0])
        except:
            self.set_status(400)
            self.finish()
            return

        try:
            accts = AccountBalances()
            net_worths = [{'date': utils.format_date(date), 'net-worth': net_worth}
                          for (date,net_worth) in accts.net_worths(start_date,end_date)]
            self.write(escape.json_encode(net_worths))
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        except:
            self.set_status(500)
        finally:
            self.finish()
