import MeCab

class mecab():
    def __init__(self):
        self.mecabType = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic')

    def execute(self, text):
        parseText = self.mecabType.parse(text)
        parseText = parseText.split("\n")
        return parseText