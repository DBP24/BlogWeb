# Scripts  Json a UTF-8
import codecs

input_file = 'mysite_data.json'
output_file = 'mysite_data_utf8.json'

with codecs.open(input_file, 'r', encoding='iso-8859-1') as f:
    content = f.read()

with codecs.open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)
