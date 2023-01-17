import json
in_filename = 'scraped_songs.json'
out_filename = 'formatted_songs_list.json'

out = open('./'+out_filename, 'w',encoding='utf-8')

with open('./'+in_filename,encoding='utf-8') as json_in:
    docs = json.loads(json_in.read())
    for doc in docs:
        out.write('%s\n' % json.dumps({'index': {}}))
        out.write('%s\n' % json.dumps(doc, indent=0,ensure_ascii=False).replace('\n', ''))
