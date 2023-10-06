import re


def fun1():
    """找到www开头.com\.edu\.net结尾的字符串"""
    list1 = ["www.baidu.com", "www.dufaeifa1231fafAA.net", "heass.fasfe13.edu",
             "www.1342fasf.edu", "www.dfase.cn"]
    for i in list1:
        result = re.match(r"www.[a-zA-Z0-9]+(.com|.edu|.net)$", i)
        if result:
            print(result.group())


def fun2():
    """找到字符开头的"""
    list1 = ["baidu.com", "dufaeifa1231fafAA.net", "13145464.fasfe13.edu",
             "_____.1342fasf.edu", "156146.dfase.cn"]
    for i in list1:
        result = re.match(r"[a-zA-Z]+", i)
        if result:
            print(result.group())


def fun3():
    """找到数字开头的"""
    list1 = ["baidu.com", "dufaeifa1231fafAA.net", "13145464.fasfe13.edu",
             "_____.1342fasf.edu", "156146.dfase.cn"]
    for i in list1:
        result = re.match(r"\d+", i)
        if result:
            print(result.group())


def fun4():
    """找到包含字母或数字的"""
    list1 = ["baidu.com", "dufaeifa1231fafAA.net", "13145464.fasfe13.edu",
             "_____.---.---", "156146.dfase.cn", "165463"]
    for i in list1:
        result = re.findall(r"[\da-zA-Z]", i)
        if result:
            print(i)


def fun5():
    """找出字符串中的时间"""
    # 不加'?:'只会打出18，返回的是列表，用serach可以不加?:返回时用com.group()
    s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
    com = re.findall(
        r'\d{4}/1?[1-9]/[1-3]?\d\s(?:0[0-9]|1[0-9]|2[0-4]):[0-5][0-9]', s)
    if com:
        print(com)


def fun6():
    """6.	将每行中的电子邮件地址替换为你自己的电子邮件地址"""
    # sub默认替换所有,可以指定个数
    # list1 = ["132131@qq.com","1431241@qq.com", "afjsefa132@qq.com", "123afdas@qq.com", "@11.com"]
    # for i in list1:
    #     ret = re.sub(r"\w*@", r"3244751057@", i)
    #     print(ret)
    ret = re.sub(r"\d", r"@", "13243fasf1231vasd123")
    print(ret)


def fun7():
    """去除html的标签"""
    content = '''
<div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p> <br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p> <br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div> 
'''
    ret = re.sub(r"<[^>]*>", r"", content)  # 其中的中括号一定要加
    print(ret)


def fun8():
    """8.	将以下网址提取出域名："""
    list1 = ["http://www.interoem.com/messageinfo.asp?id=35",
             "http://3995503.com/class/class09/news_show.asp?id=14",
             "http://lib.wzmc.edu.cn/news/onews.asp?id=769",
             "http://www.zy-ls.com/alfx.asp?newsid=377&id=6",
             "http://www.fincm.com/newslist.asp?id=415"]
    for i in list1:
        ret = re.match(r".+//([^/]+)/.+", i)
        if ret:
            print(ret.group(1))
def fun9():
    """提取出字符串中的单词"""
    stance = "hello world ha ha"
    ret = re.split(r" ", stance) # split进行分割
    print(ret)

if __name__ == '__main__':
    # fun1()
    # fun2()
    # fun3()
    # fun4()
    # fun5()
    # fun6()
    # fun7()
    # fun8()
    fun9()
