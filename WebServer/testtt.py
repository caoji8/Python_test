import configparser
cf = configparser.ConfigParser(allow_no_value=True)
cf.read('./ini/webserver.ini')
print(cf.get('host','url'))
print(cf.get('host','port'))
print(cf.get('host','localhost'))
