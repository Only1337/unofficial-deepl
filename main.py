from flask import Flask, request, jsonify
import undetected_chromedriver as uc
import selenium
from selenium.webdriver.common.by import By
import time
from urllib.parse import quote_plus

input_lang = "tr"
output_lang = "en"


app = Flask(__name__)

@app.route('/', methods=['POST'])
def translate_text():
    text = request.form.get('text')

    if not text.strip():
        return jsonify({'success': 'false', 'message': 'Text data cannot be empty'})

    text.replace("\\n", "\n")
    encoded_string = quote_plus(text)
    encoded_string = encoded_string.replace("+", "%20")
    encoded_string = encoded_string.replace("%5Cn", "%0A")

    query_string = '#' + input_lang + '/' + output_lang + '/' + encoded_string

    driver = uc.Chrome()
    driver.get('https://www.deepl.com/translator' + query_string)
    # time.sleep(1)
    while True:
        translated_text = driver.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[1]/d-textarea/div').text
        if not translated_text == "":
            break

    driver.quit()

    translated_lines = translated_text.split("\n")
    
    return jsonify({'success': 'true', 'translated': {'lines': translated_lines, 'text': translated_text}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30)
