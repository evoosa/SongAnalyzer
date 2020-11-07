from song_analyzer.song_parts.song import Song


def get_song_pos_entities(lyrics_path: str):
    song_obj = Song(lyrics_path)
    return {
        'nouns': song_obj.nouns,
        'adjectives': song_obj.adjectives,
        'noun_to_adjective_ratio': song_obj.noun_to_adj_ratio
    }
