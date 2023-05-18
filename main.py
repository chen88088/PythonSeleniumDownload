from flask import Flask, request
from selenium import webdriver
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    # 從POST資料中獲取URL
    url = request.form.get('url')

    # 使用Selenium設定瀏覽器並獲取內容
    # 啟動 Selenium 瀏覽器
    driver = webdriver.Chrome()

    def process_request():
        driver.get(url)

        # 取得網頁內容
        response_content = driver.page_source

        # 關閉瀏覽器
        driver.quit()

        # 取得網頁內容
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response_content, 'html.parser')

        # 找到所有的 <pre> 標籤
        pre_tags = soup.find_all('pre')

        # 取得第一個 <pre> 標籤的內容文字
        pre_content = pre_tags[0].get_text()

        # 返回回傳內容
        return pre_content

    webContent = process_request()
    return webContent

if __name__ == '__main__':
    app.run()
