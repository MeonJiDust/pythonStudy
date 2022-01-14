import json
"""with open('./test.txt', 'a', encoding='utf-8') as f:

    f.write('\n글이 들어가는지 또 확인')"""

with open('./test.json', 'r+', encoding='utf-8') as f:
    read_data = json.load(f)
    print(read_data)