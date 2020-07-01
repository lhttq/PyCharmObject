
from selenium import webdriver
from time import sleep
import xlrd
import os
def Excel_score(files ,rows, cols):#files:Excel文件的绝对路径；rows：起始行；cols：起始列
   # 打开文件
   x1 = xlrd.open_workbook(files)
   #输出第一个Sheet表格的名字
   print(x1.sheet_names()[0])
   #获取第一个Sheet表格的名字
   sheetName = x1.sheet_names()[0]
   #根据名字获取第一个sheet表格的内容
   content = x1.sheet_by_name(sheetName)
   #获取表格内容的所有行和列
   all_cols = content.ncols  # 列
   all_rows = content.nrows  # 行
   #循环输出表格的数据
   l = []
   for i in range(rows, all_rows - 2):
       num = content.cell(i, cols).value
       num1 = round(num, 2)
       l.append(num1)
   return l
def Excel_stu(files ,rows, cols):#files:Excel文件的绝对路径；rows：起始行；cols：起始列
   # 打开文件
   x1 = xlrd.open_workbook(files)
   #输出第一个Sheet表格的名字
   print(x1.sheet_names()[0])
   #获取第一个Sheet表格的名字
   sheetName = x1.sheet_names()[0]
   #根据名字获取第一个sheet表格的内容
   content = x1.sheet_by_name(sheetName)
   #获取表格内容的所有行和列
   all_cols = content.ncols  # 列
   all_rows = content.nrows  # 行
   #循环输出表格的数据
   l = []
   for i in range(rows, all_rows - 2):
      num = content.cell(i, cols).value
      l.append(num)
   return l
def Auto_Web(acc,password,x=[],l=[],l1=[]):#acc账号，password密码，#num学生人数
    driver = webdriver.Chrome()
    #浏览器最大化
    driver.maximize_window()
    #"http://campus.zzuli.edu.cn/pc/qy/index.html"
    #通过浏览器打开网页
    driver.get("http://campus.zzuli.edu.cn/pc/qy/index.html")
    #睡眠两秒,让网页充分加载
    sleep(2)
    #找到网页弹出的窗口
    driver.find_elements_by_css_selector("rolPopContent")
    #定位到教师网页
    driver.find_element_by_css_selector("div.choseT").click()
    #输入账号
    driver.find_element_by_id("name").send_keys(acc)
    #输入密码
    driver.find_element_by_id("password").send_keys(password)
    #sleep(2)
    #点击登录按钮
    driver.find_element_by_id("submit_login").click()
    #睡眠两秒，充分加载网页
    sleep(2)
    #进入应用中心
    driver.find_element_by_css_selector("dl.bbg2").click()
    #睡眠，充分加载网页
    sleep(2)
    #进入教务管理系统
    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/ul/li[1]/a").click()
    #由于打开新窗口，获取原窗口的值
    handle1 = driver.current_window_handle
    #获取目前所有打开窗口的值
    all_handles = driver.window_handles
    #遍历目前的所有窗口
    for handle in all_handles:
        #如果不是目前操作的窗口，关闭原来的窗口，并跳转到新窗口
        if handle != handle1:
            driver.close()
            driver.switch_to.window(handle)
    #跳转到相应的frame框架内
    driver.switch_to.frame("frmbody")
    #点击相应的菜单选项
    driver.find_element_by_id("memuBarBtn5").click()
    driver.find_element_by_xpath('//*[@id="memuLinkDiv5"]/table/tbody/tr[3]').click()
    driver.find_element_by_xpath('//*[@id="divGrpC0502"]/td/table/tbody/tr[1]/td[2]').click()
    #充分加载网页
    sleep(5)
    #重新跳入下夜歌frame
    driver.switch_to.frame("frmMain")
    #点击检索按钮
    driver.find_element_by_id("button").click()
    #加载网页
    sleep(5)
    #获取iframe的定位
    iframe = driver.find_element_by_name("frmRpt")
    #跳转到相应的框架中
    driver.switch_to.frame(iframe)
    #点击录入按钮
    driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[4]/td[9]').click()
    #加载网页
    sleep(5)
    # 获取目前操作的窗口
    h1 = driver.current_window_handle
    #获取当前所有窗口
    all_handles = driver.window_handles
    #遍历窗口
    for h in all_handles:
        print(h)
        if h != h1:
            print(h)
            #跳转到下一个窗口
            driver.switch_to.window(h)
            #获取并跳转到相应的iframe框架
            iframe = driver.find_element_by_name("frmRpt")
            driver.switch_to.frame(iframe)
            num = 0
            while 1:
                num = num + 1
                xpath = '//*[@id="hh' + str(num) + '"]/td[2]'
                try:
                    driver.find_element_by_xpath(xpath).text
                except:
                    print(num)
                    break
            j = 0
            for i in range(2, num + 1):
                j = j + 1
                xpath = '//*[@id="hh' + str(j) + '"]/td[2]'
                # 平时成绩ID
                xpath1 = "CHKPSCJ" + str(j)
                xpath2 = "CHKQMCJ" + str(j)
                # 获取学生学号
                s = driver.find_element_by_xpath(xpath).text
                #if s == x[j-1]:
                     #平时成绩
                driver.find_element_by_id(xpath1).clear()
                driver.find_element_by_id(xpath1).send_keys(int(l[j - 1]))
                     #末考成绩
                driver.find_element_by_id(xpath2).clear()
                driver.find_element_by_id(xpath2).send_keys(int(l1[j - 1]))
            driver.switch_to.default_content()
            #暂存按钮
            driver.find_element_by_name("btn_save").click()
            sleep(10)
            #两次确认
            driver.switch_to.alert.accept()
            driver.switch_to.alert.accept()

l1 = Excel_score("F:\lht\Desktop\kjx.xlsx",1,7)
l2 = Excel_score("F:\lht\Desktop\kjx.xlsx",1,8)
x1 = Excel_stu("F:\lht\Desktop\kjx.xlsx",0,1)

Auto_Web("","",x1,l1,l2)
#以下是测试代码
            # driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[2]/td[9]').click()
            # sleep(5)
            # driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[3]/td[9]').click()
            #
            # sleep(5)
            # driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[4]/td[9]').click()