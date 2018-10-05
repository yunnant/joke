# coding=utf-8
import itchat, time, re,threading
from  itchat.content import *
from datetime import datetime, timedelta
import urllib.request,urllib
import random
plan_dict={}
dict2={u'一':1,u'二':2,u'三':3,u'四':4,u'五':5,u'六':6,(u'七',u'日',u'天'):7,u'八':8,u'九':9,u'0':0}
@itchat.msg_register([TEXT])
def plan_reply(msg):
    global joke_times
    info = msg['Text']
    b0=info.find(u'桂杨');b1=info.find(u'笑话')
    if b0>=0:itchat.send(u'桂杨嘤嘤嘤 \n♥(๑> ₃ <)♥\n✨(۶•౪•)۶💗٩(•౪•٩)✨\n（づ￣3￣）づ╭❤～', msg['FromUserName'])
    if b1 >= 0:
        content_clear=[]
        for i in range(1,2):
            url = "https://www.qiushibaike.com/text/page/" + str(i)
            content =getcontent(url)
            content_clear +=content
        #content_clear=getcontent(url)
        #print(len(content_clear))
        joke_times+=1
        if joke_times>=20:joke_times=0
        joke=content_clear[joke_times]
        itchat.send(joke,msg['FromUserName'])



def getcontent(url):
    time.sleep(2)
    # 模拟成浏览器
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    # 将opener安装为全局
    urllib.request.install_opener(opener)

    # 解码为中文
    data = urllib.request.urlopen(url).read().decode("utf-8")

    # 构建对应用户提取的正则表达式
    #userpat = '<div class="author clearfix">.+?</div>'

    # 构建段子内容提取的正则表达式
    contentpat = '<div class="content">.+?</div>'

    #userlist = re.compile(userpat, re.S).findall(data)
    contentlist = re.compile(contentpat, re.S).findall(data)

    # 单个用户
    singlepat = '<h2>\\n[^\s]+\\n</h2>'
    # 单个内容
    singlecon = '<span>\\n\\n\\n[^\s]+\\n\\n</span>'

    x = 1
    content_clear=[]
    for single_content in contentlist:
        content_clear.append ( str(re.compile(singlecon, re.S).findall(single_content)).replace("['<span>\\n\\n\\n", "").replace("\\n\\n</span>']", "").replace("<br/>", ""))
        x+=1#name = "content" + str(x)
    while '[]' in content_clear:
        content_clear.remove('[]')
    #joke_times+=1
    return content_clear
        # 不明白
        # name += content_clear?
        #exec(name + '=content_clear')
        #name + '=content_clear'
        #x += 1

    '''y = 1
    # 通过for循环遍历用户，并输出该用户对应的内容
    #print(userlist)
    for single_user in userlist:
        user_clear = str(re.compile(singlepat, re.S).findall(single_user)).replace("['<h2>\\n", '').replace("\\n</h2>']", '')
        name = "content" + str(y)
        #print("用户 " + str(page) + "_" + str(y) + " 是:" + user_clear)
        #print("内容是：")

        # 不明白
        exec("print("+name+")")
        print("\n")
        y += 1'''

joke_times=0
itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run(debug=True)
