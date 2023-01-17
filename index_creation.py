from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re,os
client = Elasticsearch("https://localhost:9200", http_auth=('elastic','RSzrHv-bZ5+Vuv2_sTGo'), use_ssl = False, ca_certs = False, verify_certs = False)
INDEX = 'songs'


def createIndex():
    settings = {
    "settings": {
        "index": {
          "analysis": {
            "analyzer": {
              "sinhalaAnalyzer": {
                "type": "custom",
                "tokenizer": "icu_tokenizer"
              }
            }
          }
        }
      },
    "mappings": {
        "properties": {
            "title": {
                "type": "text",
                "fields":{
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                },
                "analyzer": "sinhalaAnalyzer",
                "search_analyzer": "standard"
            },
            "artist": {
                "type": "text",
                "fields":{
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                },
                "analyzer": "sinhalaAnalyzer",
                "search_analyzer": "standard"
            },
            "lyrics_by": {
                "type": "text",
                "fields":{
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                },
                "analyzer": "sinhalaAnalyzer",
                "search_analyzer": "standard"
            },
            "music_by": {
                "type": "text",
                "fields":{
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                },
                "analyzer": "sinhalaAnalyzer",
                "search_analyzer": "standard"
            },
            "metaphors":{
                "type": "nested",
                "properties":{
                    "name": {
                        "type": "text",
                        "fields":{
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer": "sinhalaAnalyzer",
                        "search_analyzer": "standard"
                      },
                    "source": {
                        "type": "text",
                        "fields":{
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer": "sinhalaAnalyzer",
                        "search_analyzer": "standard"
                      },
                    "target": {
                        "type": "text",
                        "fields":{
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer": "sinhalaAnalyzer",
                        "search_analyzer": "standard"
                    },
                    "interpretation": {
                        "type": "text",
                        "fields":{
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer": "sinhalaAnalyzer",
                        "search_analyzer": "standard"
                    }
                }
            },
            "song_lyrics": {
                "type": "text",
                "fields":{
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                },
                "analyzer": "sinhalaAnalyzer",
                "search_analyzer": "standard"
            } 
        }
    }
}


    # index = Index(INDEX,using=client)
    # result = index.create()
    result = client.indices.create(index=INDEX , body =settings)
    print (result)


def read_translated_songs():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file1 = os.path.join(THIS_FOLDER, 'data')
    my_file = os.path.join(my_file1, 'scraped_songs.json')
    
    with open(my_file,'r',encoding='utf8') as tra_file:
        tra_songs = json.loads(tra_file.read())
        results_list = [a for num, a in enumerate(tra_songs) if a not in tra_songs[num + 1:]]
        return results_list


def clean_function(song_lyrics):
    if (song_lyrics):
        processed_list = []
        song_lines = song_lyrics.split('\n')
        
        for place,s_line in enumerate(song_lines):
            process_line = re.sub('\s+',' ',s_line)
            punc_process_line = re.sub('[.!?\\-]', '', process_line)
            processed_list.append(punc_process_line)
        
        sen_count = len(processed_list)
        final_processed_list = []
        
        for place,s_line in enumerate(processed_list):
            if (s_line=='' or s_line==' '):
                if (place!= sen_count-1 and (processed_list[place+1]==' ' or processed_list[place+1]=='')) :
                    pass
                else:
                    final_processed_list.append(s_line)
            else:
                final_processed_list.append(s_line)
        final_song_lyrics = '\n'.join(final_processed_list)
        return final_song_lyrics
    else:
        return None

def data_generation(song_array):
    for song in song_array:
        title = song["title"]
        song_lyrics = clean_function(song["song_lyrics"])
        artist = song["artist"]
        lyrics_by = song["lyrics_by"]
        music_by = song["music_by"]
        metaphor_array = song["metaphors"]
        for metaphor in metaphor_array:
            name = metaphor["name"]
            source = metaphor["source"]
            target = metaphor["target"]
            interpretation = metaphor["interpretation"]

            yield {
                "_index": INDEX,
                "_source": {
                    "title": title,
                    "song_lyrics": song_lyrics,
                    "artist": artist,
                    "lyrics_by": lyrics_by,
                    "music_by": music_by,
                    "_metaphors": {
                        "name" : name,
                        "source": source,
                        "target" : target,
                        "interpretation" : interpretation
                    }
                }
            }


createIndex()
translated_songs = read_translated_songs()
helpers.bulk(client,data_generation(translated_songs))