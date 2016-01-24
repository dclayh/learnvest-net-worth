from tornado.ioloop import IOLoop
from tornado.web import Application

from handlers.net_worth_handler import NetWorthHandler

HOST = '0.0.0.0'
PORT = '80'


def main():

    application = Application([
                (r"/net-worth/", NetWorthHandler),
                ])

    application.listen(int(PORT), address=HOST, xheaders=True)

    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

