# Unofficial DeepL Translator API

This repository contains a Flask application that utilizes the DeepL translation service to translate text from one language to another. The application uses Selenium and undetected_chromedriver library to automate the translation process.

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/Only1337/deepl-translator.git
   ```

2. Install the required dependencies. Make sure you have Python and pip installed. Use the following command to install the dependencies:

   ```
   pip install flask undetected_chromedriver selenium
   ```

3. Run the Flask application:

   ```
   python app.py
   ```

   The application will start running on `http://localhost:30`.

4. Make a POST request to the root endpoint with the following parameters:

   - `text`: The text you want to translate.

   Example using cURL:

   ```bash
   curl -X POST -d "text=Merhaba Dünya!" http://localhost:30
   ```

   The response will be a JSON object containing the translated text.

## Configuration

Before running the application, you can modify the following variables in the code to customize the translation:

- `input_lang`: The input language code. Change this to the appropriate language code (e.g., `"en"`, `"fr"`, `"es"`).
- `output_lang`: The output language code. Change this to the appropriate language code.
- `port`: The port on which the Flask application will run. Change this if necessary.

Please note that the code is currently set to use Turkish (`"tr"`) as the input language and English (`"en"`) as the output language. Modify the language codes as per your requirements.

## Disclaimer

This application is for educational purposes only. Use it responsibly and comply with the terms and conditions of the DeepL service.

**Note:** The `undetected_chromedriver` library is used to bypass certain anti-automation measures. Make sure you understand the implications and legalities of using such tools before proceeding.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
