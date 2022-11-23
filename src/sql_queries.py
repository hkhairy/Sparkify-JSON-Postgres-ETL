# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS user_table;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time_table;"

# CREATE TABLES

# TODO is the songplay a primary Key? What are the datatypes of this table?
# TODO is the level column necessary? I don't think it is.
songplay_table_create = ("""
                         CREATE TABLE IF NOT EXISTS songplay(
                             songplay_id INT,
                             start_time FLOAT,
                             user_id VARCHAR references user_table(user_id),
                             level INT,
                             song_id VARCHAR references song(song_id),
                             artist_id VARCHAR references artist(artist_id),
                             session_id INT,
                             location VARCHAR,
                             user_agent VARCHAR
                         );
""")

user_table_create = ("""
                     CREATE TABLE IF NOT EXISTS user_table(
                         user_id VARCHAR PRIMARY KEY,
                         first_name VARCHAR,
                         last_name VARCHAR,
                         gender VARCHAR(1),
                         level INT
                     );
""")


artist_table_create = ("""
                       CREATE TABLE IF NOT EXISTS artist(
                           artist_id VARCHAR PRIMARY KEY,
                           name VARCHAR,
                           location VARCHAR,
                           latitude FLOAT,
                           longitude FLOAT
                       );
""")

song_table_create = ("""
                     CREATE TABLE IF NOT EXISTS song(
                         song_id VARCHAR PRIMARY KEY,
                         title VARCHAR,
                         artist_id VARCHAR references artist(artist_id),
                         year INT,
                         duration FLOAT
                     );
""")

# TODO I'm not sure about this table's datatypes, or even its existence
# TODO Maybe we need a lot of constraints here
time_table_create = ("""
                     CREATE TABLE IF NOT EXISTS time_table(
                         start_time FLOAT,
                         hour INT,
                         day INT,
                         week INT,
                         year INT,
                         weekday INT
                     );
""")

# INSERT RECORDS

songplay_table_insert = ("""
                         INSERT INTO songplay (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location VARCHAR, user_agent)
                         VALUES (%s, %f, %s, %d, %s, %s, %s, %s, %s)
                         """)

user_table_insert = ("""

""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, artist_table_drop, song_table_drop, time_table_drop, songplay_table_drop]