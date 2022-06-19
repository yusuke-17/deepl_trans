import deepl
import os

API_KEY = ''
translator = deepl.Translator(API_KEY)

# 翻訳したい言語
source_lang = 'DE'
# 翻訳した言語
target_lang = 'JA'
# 翻訳したいファイル名
trans_file = 'trans.txt'


def main():
    source_file = 'trans/' + trans_file
    file_name = os.path.splitext(os.path.basename(source_file))[0]
    root, ext = os.path.splitext(source_file)
    target_file = 'result/' + file_name + '_' + target_lang + ext

    # 翻訳開始
    translator.translate_document_from_filepath(
        source_file,
        target_file,
        source_lang=source_lang,
        target_lang=target_lang
    )


if __name__ == "__main__":
    main()
