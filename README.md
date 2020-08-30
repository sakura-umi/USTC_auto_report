# USTC_auto_report

##简述
中科大健康打卡selenium版
推荐挂在吃灰的服务器上

##使用方法
1. 下载安装chromedriver
    ###下载
    ####CDN
   `wget https://v.srprpr.ga/chromedriver`
    ####github
    `wget https://`
    
    ###安装
    `mv chromedriver /usr/bin`
2. 安装python3，selenium库
    ---
    yum install python3
    pip3 install selenium
    ---
3. 下载py脚本文件，填入账号密码。
4. 安装设置定时任务
    ---
    yum install crontabs
    crontab -e
    ---
    在下面添加一行
    `0 0,6,12,18 * * * /usr/bin/python3 py脚本所在路径(绝对路径)`
    即可
    
