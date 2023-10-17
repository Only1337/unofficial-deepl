from flask import Flask, request, jsonify
import requests as r

session = r.session()

show_other_translations = False # if you want to show other translations, set this to True (it will be slower)

def translate(text, input_lang, output_lang):
    # i make a request to the deepl translate without the api key
    # and i get the cookie from the response
    session.get("https://www.deepl.com/translator")
    # then i make a request to the deepl translate with the api key
    # and the cookie from the previous request
    response = session.post(
        "https://www2.deepl.com/jsonrpc",
        json={
            "jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "jobs": [
                    {
                        "kind": "default",
                        "raw_en_sentence": text,
                        "raw_en_context_before": [],
                        "raw_en_context_after": [],
                        "preferred_num_beams": 4,
                        "quality": "fast",
                    }
                ],
                "lang": {
                    "user_preferred_langs": ["DE", "EN"],
                    "source_lang_user_selected": input_lang.upper(),
                    "target_lang": output_lang.upper(),
                },
                "priority": -1,
                "commonJobParams": {},
                "timestamp": 1623621579000,
            },
            "id": 40890006,
        },
    )

    # i get the translated text from the response
    # translated_text = response.json()["result"]["translations"][0]["beams"][0]["postprocessed_sentence"]

    if show_other_translations:
        translate_response = {
            "text": response.json()["result"]["translations"][0]["beams"][0]["postprocessed_sentence"],
            "other_translations": {}
        }

        index = 0
        for i in response.json()["result"]["translations"][0]["beams"]:
            if not index == 0:
                translate_response["other_translations"][index-1] = i["postprocessed_sentence"]
            index += 1

        return translate_response
    else:
        if response.json()["message"] == "Too many requests":
            return "Too many requests."
            
        translated_text = response.json()["result"]["translations"][0]["beams"][0]["postprocessed_sentence"]
        return translated_text


# print(translate("""Bu gün nasılsın dostum?\nBu bir satır denemesidir.""", "TR", "EN"))

app = Flask(__name__)

@app.route('/', methods=['POST'])
def translate_text():
    text = request.form.get('text')
    input_lang = request.form.get('input_lang').upper()
    output_lang = request.form.get('output_lang').upper()

    if not text.strip():
        return jsonify({'success': 'false', 'message': 'Text data cannot be empty'})
    
    translated_data = translate(text, input_lang, output_lang)
    
    return jsonify({'success': 'true', 'translated': {'text': translated_data}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30)
