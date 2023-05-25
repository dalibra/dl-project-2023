class Translator:

    def translate(self, request, dest):
        from requests import get
        import json

        response = get('https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl={}&q={}'.format(dest, request))
        trans_sentences = json.loads(response.text)[0]

        return '. '.join(trans_sentences)[:-3]


translator = Translator()
