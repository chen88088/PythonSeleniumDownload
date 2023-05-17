from flask import Flask, request
from selenium import webdriver
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    url = request.form.get('url')  # 從POST資料中獲取URL
    # post_data = request.form.get('post_data')  # 從POST資料中獲取POST資料參數

    # 使用Selenium設定瀏覽器並獲取內容
    # 啟動 Selenium 瀏覽器
    driver = webdriver.Chrome()
    driver.get(url)

    # 取得網頁內容
    response_content = driver.page_source

    # 將POST資料傳遞給網頁表單
    # input_element = driver.find_element_by_name('input')  # 假設表單中的輸入欄位名稱為'input'
    # input_element.send_keys(post_data)
    # input_element.submit()

    # 等待網頁處理後的回傳內容
    # result_element = driver.find_element_by_id('result')  # 假設回傳內容位於id為'result'的元素中
    # result = result_element.text

    driver.quit()  # 關閉瀏覽器

    # 取得網頁內容

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response_content, 'html.parser')

    # 找到所有的 <pre> 標籤
    pre_tags = soup.find_all('pre')

    # 取得第一個 <pre> 標籤的內容文字
    pre_content = pre_tags[0].get_text()

    # 返回回傳內容
    return pre_content


if __name__ == '__main__':
    app.run()
