# coding=<encoding name> ： # coding=utf-8
from datetime import datetime
import requests
import json
import smtplib
from email.mime.text import MIMEText

base_url = 'https://leetcode-cn.com'
# 获取今日每日一题的题名(英文)
response = requests.post(base_url + "/graphql", json={
    "operationName": "questionOfToday",
    "variables": {},
    "query": "query questionOfToday { todayRecord {   question {     questionFrontendId     questionTitleSlug     __typename   }   lastSubmission {     id     __typename   }   date   userStatus   __typename }}"
})
leetcodeTitle = json.loads(response.text).get('data').get('todayRecord')[0].get("question").get('questionTitleSlug')

# 获取今日每日一题的所有信息
url = base_url + "/problems/" + leetcodeTitle
response = requests.post(base_url + "/graphql",
                         json={"operationName": "questionData", "variables": {"titleSlug": leetcodeTitle},
                               "query": "query questionData($titleSlug: String!) {  question(titleSlug: $titleSlug) {    questionId    questionFrontendId    boundTopicId    title    titleSlug    content    translatedTitle    translatedContent    isPaidOnly    difficulty    likes    dislikes    isLiked    similarQuestions    contributors {      username      profileUrl      avatarUrl      __typename    }    langToValidPlayground    topicTags {      name      slug      translatedName      __typename    }    companyTagStats    codeSnippets {      lang      langSlug      code      __typename    }    stats    hints    solution {      id      canSeeDetail      __typename    }    status    sampleTestCase    metaData    judgerAvailable    judgeType    mysqlSchemas    enableRunCode    envInfo    book {      id      bookName      pressName      source      shortDescription      fullDescription      bookImgUrl      pressImgUrl      productUrl      __typename    }    isSubscribed    isDailyQuestion    dailyRecordStatus    editorType    ugcQuestionId    style    __typename  }}"})
# 转化成json格式
jsonText = json.loads(response.text).get('data').get("question")
# 题目题号
no = jsonText.get('questionFrontendId')
# 题名（中文）
leetcodeTitle = jsonText.get('translatedTitle')
# 题目难度级别
level = jsonText.get('difficulty')
# 题目内容
context = jsonText.get('translatedContent')

# print(leetcodeTitle)
# print(context)
# print(level)
# print(no)

# 早安语录接口（天行数据API）
response = requests.get("http://api.tianapi.com/txapi/zaoan/index?key=" + "fa153051d08c72f2469647415f10a216")
json = json.loads(response.text)
# 得到语录数据
ana = json.get('newslist')[0].get('content')
# 表情链接
face_url = 'http://wx3.sinaimg.cn/large/007hyfXLly1g0uj7x5jpaj301o02a0sw.jpg'

# 开始运行时间
begin_time = datetime(2020, 12, 23)
# 脚本运行时间计算
info = "<span style='color:cornflowerblue'>本脚本已运行{0}天<span>".format(
    (datetime.today() - begin_time).days.__str__())

# 数据全部HTML化
htmlText = """ <head>
        <meta charset=UTF-8>
        <link rel="stylesheet">
        <style>
            code {
                color: blue;
                font-size: larger;
            }
        </style>
        </link>
    </head>
    <body>
    <div> </B><BR></B><FONT
            style="FONT-SIZE: 12pt; FILTER: shadow(color=#af2dco); WIDTH: 100%; COLOR: #730404; LINE-HEIGHT: 100%; FONT-FAMILY: 华文行楷"
            size=6><span style="COLOR: cornflowerblue">早安语录:</span>""" + ana + """</FONT><img width="40px"  src=""" + face_url + """">
<div>
    <h3>Leetcode-每日一题</h3>
    <h4>""" + no + '.' + leetcodeTitle + '.' + level + """</h4>""" + context + '本题连接：<a href=' + url + ">" + url + "</a></div>" + info


# print(htmlText)


# 邮箱类
class SendEmail:
    def __init__(self, show_name, send_user, email_host, email_port, password, user_list, title, message):
        self.show_name = show_name
        self.send_user = send_user
        self.email_host = email_host
        self.email_port = email_port
        self.password = password
        self.user_list = user_list
        self.message = message
        self.title = title

    def send_email(self):
        try:
            user = self.show_name + "<" + self.send_user + ">"
            message = MIMEText(self.message, _subtype='html', _charset='utf-8')
            message['Subject'] = self.title
            message['From'] = user
            message['To'] = ";".join(self.user_list)
            server = smtplib.SMTP_SSL(self.email_host)
            server.connect(self.email_host, self.email_port)
            server.login(self.send_user, self.password)
            server.sendmail(user, self.user_list, message.as_string())
            server.close()
            print("success!!!")
        except Exception as e:
            print("error:", e)


if __name__ == '__main__':
    # 发件人邮箱
    send_user = ""
    # 邮箱对应的host
    email_host = "smtp.qq.com"
    email_port = 465
    # 开启SMTP时的密码
    password = ""
    # 邮件上显示的昵称
    show_name = "小灿智能助手"
    # 收件人邮箱账户（可多人）
    user_list = [""]
    # 邮件标题
    title = "每日信息推送"
    message = htmlText
    send = SendEmail(show_name, send_user, email_host, email_port, password, user_list, title, message)
    send.send_email()
