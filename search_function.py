from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re,os
import advanced_queries
client = Elasticsearch("https://localhost:9200", http_auth=('elastic','RSzrHv-bZ5+Vuv2_sTGo'), use_ssl = False, ca_certs = False, verify_certs = False)
INDEX = 'songs'

synonym_artist = ['ගායකයා','ගයනවා','ගායනා','ගයනා','ගැයු','ගයන','ගයපු']
synonym_lyrics_by = ['ගත්කරු','රචකයා','ලියන්නා','ලියන','රචිත','ලියපු','ලියව්‌ව','රචනා','රචක','ලියන්','ලියූ']
synonym_music_by = ['සංගීත','සංගීතවත්','සංගීතය']

synonym_list = [synonym_artist,synonym_lyrics_by,synonym_music_by]

def search(search_query):
    processed_query = ""
    tokens = search_query.split()
    processed_tokens = search_query.split()
    search_fields = []
    sort_num = 0
    field_list = ["artist","lyrics_by","music_by"]
    all_fields = ["title","song_lyrics","metaphors","artist","lyrics_by","music_by"]
    final_fields = []

    for word in tokens:
        print (word)

        for i in range(0, 3):
            if word in synonym_list[i]:
                print('Adding field', field_list[i], 'for ', word, 'search field list')
                search_fields.append(field_list[i])
                processed_tokens.remove(word)

    if (len(processed_tokens)==0):
        processed_query = search_query
    else:
        processed_query = " ".join(processed_tokens)

    final_fields = search_fields


    if(len(search_fields)==0):
        query_es = advanced_queries.multi_match_agg_cross(processed_query, all_fields)
    elif (len(search_fields) == 2):
        query_es = advanced_queries.multi_match_agg_phrase(processed_query, all_fields)
    else:
        query_es = advanced_queries.multi_match_agg_cross(processed_query, final_fields)

    print("QUERY BODY")
    print(query_es)
    search_result = client.search(index=INDEX, body=query_es)
    return search_result




