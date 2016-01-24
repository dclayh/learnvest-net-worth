FROM python:2.7-onbuild

EXPOSE 80

CMD [ "python", "./net_worth.py" ]
