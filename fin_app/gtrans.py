from deep_translator import GoogleTranslator

SUPPORTED_LANGS = ['en', 'hi', 'kn', 'mr', 'bn']
translation_cache = {}
def translate_text(text, target_lang):
    key = (text, target_lang)
    if key in translation_cache:
        return translation_cache[key]
    # Set default language if target_lang is None or invalid
    #if not target_lang or target_lang not in SUPPORTED_LANGS:
    #    target_lang = 'en'
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        translation_cache[key] = translated
        return translated
        #return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        print(f"translation error: {e}")
        return text
