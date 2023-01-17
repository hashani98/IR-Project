import json


def multi_match(query, fields=['title','song_lyrics'], operator ='or'):
	q = {
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": operator,
				"type": "best_fields"
			}
		}
	}
	return q
    
    
def multi_match_agg_best(query, fields=['title','song_lyrics']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 105,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
		"aggs": {
			"Music Filter": {
				"terms": {
					"field": "music_by.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics_by.keyword",
					"size": 10
				}
			},
            "MetaphorName Filter" : {
                "terms": {
                    "field" : "name.keyword",
                    "size" : 10
                }
            },
            "MetaphorSource Filter" : {
                "terms": {
                    "field" : "source.keyword",
                    "size" : 10
                }
            },
            "MetaphorTarget Filter" : {
                "terms": {
                    "field" : "target.keyword",
                    "size" : 10
                }
            },
            "MetaphorInterpretation Filter" : {
                "terms": {
                    "field" : "interpretation.keyword",
                    "size" : 10
                }
            },
		}
	}

	q = json.dumps(q)
	return q

def multi_match_agg_cross(query, fields=['title','song_lyrics']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 105,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Music Filter": {
				"terms": {
					"field": "music_by.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics_by.keyword",
					"size": 10
				}
			},
            "MetaphorName Filter" : {
                "terms": {
                    "field" : "name.keyword",
                    "size" : 10
                }
            },
            "MetaphorSource Filter" : {
                "terms": {
                    "field" : "source.keyword",
                    "size" : 10
                }
            },
            "MetaphorTarget Filter" : {
                "terms": {
                    "field" : "target.keyword",
                    "size" : 10
                }
            },
            "MetaphorInterpretation Filter" : {
                "terms": {
                    "field" : "interpretation.keyword",
                    "size" : 10
                }
            },
		}
	}

	q = json.dumps(q)
	return q
