# leetcode-every-day-auto-push
leetcode每日一题推送
把文件上传到服务器并配置定时任务**

 - 确保crontab的安装详细可查看这篇博客（[crontab安装及操作](https://blog.csdn.net/hukai0q/article/details/83380951)）
 - 在linux环境下用pip安装我们的脚本所需要用到模块如：**pip install requests**
 - 查看python的安装目录：**which python**
 - 配置定时任务：**crontab -e**
 - 输入：格式：分 时 日 月 星期几 python安装目录 脚本目录
             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
   如：**00  8 * * * /usr/bin/python /root/download/init.py** （每天早上8点运行脚本）
 - 查看任务列表：crontab -l
