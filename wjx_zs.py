# 导入必要的库
from selenium import webdriver  # 导入webdriver模块
from selenium.webdriver.common.by import By  # 导入By类，用于定位元素
from selenium.common.exceptions import *  # 导入异常处理类
import time  # 导入时间模块
 
# 初始化标志位和浏览器选项
flag = 0
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 添加Chrome选项，排除自动化测试提示
option.add_experimental_option('useAutomationExtension', False)  # 添加Chrome选项，关闭自动化扩展
browser = webdriver.Chrome(options=option)  # 启动Chrome浏览器并设置选项
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
                         })  # 在新文档中执行JavaScript代码，以隐藏WebDriver特征
 
# 定义自动填充函数
def autoFillSpace(username, sid, phone):
    browser.get(url)  # 打开指定URL
    time.sleep(0.1)  # 等待页面加载
    answers = browser.find_elements(By.CSS_SELECTOR, ".ui-field-contain")  # 查找所有问题元素
    i = 0  # 计数器初始化为0
    for answer in answers:  # 遍历每个问题元素
        try:
            i += 1  # 计数器递增
            browser.execute_script("arguments[0].scrollIntoView();", answer)  # 将问题元素滚动到视图中
            title = answer.find_element(By.CSS_SELECTOR, ".field-label")  # 获取问题标题元素
            print(title.text)  # 打印问题标题文本
            if ("姓名" in title.text or "名字" in title.text):  # 如果标题中包含"姓名"或"名字"
                idfind = "q%d" % i  # 构造问题元素ID
                a = browser.find_element(By.ID, idfind)  # 查找问题输入框元素
                a.send_keys(username)  # 在输入框中输入姓名
            elif ("学号" in title.text):  # 如果标题中包含"学号"
                idfind = "q%d" % i  # 构造问题元素ID
                browser.find_element(By.ID, idfind).send_keys(sid)  # 在输入框中输入学号
            elif ("手机" in title.text or "电话" in title.text):  # 如果标题中包含"手机"或"电话"
                idfind = "q%d" % i  # 构造问题元素ID
                browser.find_element(By.ID, idfind).send_keys(phone)  # 在输入框中输入电话号码
        except Exception as e:  # 捕获异常
            print(e)  # 打印异常信息

    try:
        am = browser.find_element(By.XPATH, "//*[@id='ctlNext']")  # 查找下一步按钮元素
        am.click()  # 点击下一步按钮
    except:
        return 0  # 如果找不到按钮元素，返回0

    time.sleep(0.1)  # 等待页面加载

    try:
        browser.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]').click()  # 关闭弹窗
        time.sleep(1)  # 等待页面加载
    except:
        pass

    try:
        browser.find_element(By.XPATH, '//*[@id="SM_BTN_WRAPPER_1"]').click()  # 提交表单
        time.sleep(3)  # 等待页面加载
    except:
        pass
    print("finish!")  # 打印填写完成信息
    return 1  # 返回填写完成标志位
 
if __name__ == '__main__':
    url = 'https://www.wjx.cn'  # 设置目标网页的URL
    username = u'Your Name'  # 设置姓名
    sid = 'Student ID'  # 设置学号
    phone = 'Mobile Phone'  # 设置手机号
    cnt = 0  # 初始化计数器为0
    while True:  # 进入循环
        flag = autoFillSpace(username, sid, phone)  # 调用自动填充函数
        if flag == 1:  # 如果填写完成
            time.sleep(10)  # 等待10秒
            break  # 跳出循环
        else:  # 如果未填写完成
            cnt += 1  # 计数器递增
            print(f'时间未到{cnt + 1}')  # 打印等待信息
