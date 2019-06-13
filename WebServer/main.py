from aiohttp import web
import asyncio
import urllib.parse
import re
import json
from WebServer.model.StudentMassage import Datebase
from jinja2 import Environment,FileSystemLoader
import configparser
from sqlite3 import connect
import logging
async def login(request):
    print(request.message.path)
    with open('./views/login.html', 'r', encoding='utf-8') as op:
        data = op.read()
    return web.Response(body=data,content_type='text/html')
async def register(request):
    print(request.message.url)
    with open('./views/register.html', 'r', encoding='utf-8') as op:
        data = op.read()
    return web.Response(body=data, content_type='text/html')
async def selectAll(request):
    model = Datebase('Message')
    date = model.selectAllMassage()
    env = Environment(loader=FileSystemLoader('./views'))
    template = env.get_template('selectAll.html')
    veiw = template.render(**locals())
    return web.Response(body=veiw,content_type='text/html')
# 处理判断并返回页面
async def check(request):
    print(request)
    requestPath= request.message.path
    message = urllib.parse.unquote(requestPath)
    reJson = re.compile('\[.+\]')
    ajaxJson = re.findall(reJson,message)[0]
    test = re.sub('\'', '\"', ajaxJson)
    ajaxJson = json.loads(test)
    username = ajaxJson[0]['username']
    password = ajaxJson[1]['password']
    model = Datebase('Message')
    model.creatDatebase()
    if(model.selectPassword(username=username,password=password)):
        return web.Response(body='true',content_type='text/plain')
    else:
        return web.Response(body='false',content_type='text/plain')
#     这个check 函数用来处理ajax的请求 将结果返回给页面 然后页面根据 返回的值进行判断并且 改变页面中的元素 或者对页面进行跳转
#   python ajax 解决
async def registeruser(request):
    telephone = urllib.parse.parse_qs(request.query_string)['telephone'][0]
    print(telephone)
    age = urllib.parse.parse_qs(request.query_string)['age'][0]
    password = urllib.parse.parse_qs(request.query_string)['password'][0]
    username = urllib.parse.parse_qs(request.query_string)['lastname'][0]
    job = urllib.parse.parse_qs(request.query_string)['job'][0]
    gender = urllib.parse.parse_qs(request.query_string)['city'][0]
    if(gender == '1'):
        gender = '男'
    else:
        gender='女'
    model = Datebase('Message')
    model.inserMassage(username=username,password=password,age=int(age),gender=gender,job=job,telephone=int(telephone))
    with open('./views/success.html', 'r', encoding='utf-8') as op:
        data = op.read()
    return web.Response(body=data, content_type='text/html')
async def success(requset):
    with open('./views/success.html', 'r', encoding='utf-8') as op:
        data = op.read()
    return web.Response(body=data, content_type='text/html')
async def init(loop):
    app = web.Application()
    # 当请求过来后 注册处理的路由
    app.router.add_route('GET', '/',login)
    app.router.add_route('GET', '/login', login)
    app.router.add_route('GET','/register',register)
    app.router.add_route('GET', '/check', check)
    app.router.add_route('GET','/selectAll',selectAll)
    app.router.add_route('GET','/registeruser',registeruser)
    app.router.add_route('GET','/success',success)
    runner = web.AppRunner(app)
    # 此处打断点为了多用户执行
    cf = configparser.ConfigParser(allow_no_value=True)
    cf.read('./ini/webserver.ini')
    await runner.setup()
    print(cf.get('host','url'))
    host = cf.get('host','localhost')
    port = cf.get('host','port')
    message = 'http://localhost:9002'
    logging.basicConfig(filename='webserver',level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info(message)
    site = web.TCPSite(runner,host=host,port=port)
    await site.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


