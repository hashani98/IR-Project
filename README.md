# IR-Project

Song Search Engine using ElasticSearch and Python for IR Project(CS4642)

## Getting Start
### Setting up the Environment
* Download and Install the _ElasticSearch_
* Install the _ICU_Tokenizer_ plugin on the ElasticSearch
* Install the _python3_ with _pip3_
* Install the python packages in the _requirements.txt_

### Running the Project
1. First start the ElasticSearch locally on port 9200.
2. Then run **_index_creation.py_** file to create the index and insert data.
3. Next run the **_main.py_** to start the search engine
4. Then visit http://localhost:5000/ for see the user interface.
5. Finally add your search query in the search box for searching.

## File Structure
* songcorpus - Folder contains python codes used for scrape data
* templates - Folder contains Html user interface of the search engine
* index_creation.py - Python code for index creating and data inserting
* search_function.py - Python code use for process search query
* advanced_queries.py - Elastic Search queries

## Details of Song Data
scraped_songs.json file contains 105 Sinhala Songs with the following data.
1. title - Song title in both Sinhala and English languages
2. song_lyrics - Song lyrics in Sinhala
3. artist - Singer's name in Sinhala
4. lyrics_by - Lyricist's name in Sinhala
5. music_by - Musician's name in Sinhala
6. name - metaphor
7. source - metaphor source
8. target - metaphor target
9. interpretation - metaphor interpretation

## Basic Functionalities
* It supports searching by the title, artist name, writer name, composer name, or using the part of the lyrics.(Faceted Query)
> eg : රන් ටිකිරි සිනා
* Search Engine can identify synonyms related to specific fields like ගයපු(artist), ලියපු(lyricist), සංගීත(music) and search
based on the identified fields
> eg : ගුණදාස කපුගේ ගයපු සින්දු, ලුෂන් බුලත්සිංහල ලියූ සින්දු, එච්.එම්. ජයවර්ධන සංගීතවත් කල ගී
* Search Engine also shows metaphors in each song with their source domain, target domain and interpretation
> eg : 
