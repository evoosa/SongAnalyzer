from song_analyzer.song_parts.song import Song


def get_song_pos_entities(lyrics_path: str) -> dict:
    """
    Get POS entities data for a given song
    :param lyrics_path: path to the lyrics file
    :return:
    """
    song_obj = Song(lyrics_path)
    return dict(
        nouns=song_obj.nouns,
        adjectives=song_obj.adjectives,
        noun_to_adjective_ratio=song_obj.noun_to_adj_ratio
    )

def get_length_stats(lyrics_path: str) -> dict[str, int]:
    """
    Get statistics about the min/max/average length of the sentences and words in the song
    :param lyrics_path: path to the lyrics file
    :return:
    """
    """
    ::
    :return: sentences statistics
    """
    song_obj = Song(lyrics_path)
    sentences_lengths = [len(sentence.words) for sentence in song_obj.sentences]
    sen_max_len = max(sentences_lengths)
    sen_min_len = min(sentences_lengths)
    sen_average_len = sum(sentences_lengths) / len(sentences_lengths)

    words_lengths = []
    for sentence in song_obj.sentences:
        for word in sentence.words:
            words_lengths.append(len(word.data))
    word_max_len = max(words_lengths)
    word_min_len = min(words_lengths)
    word_average_len = sum(words_lengths) / len(words_lengths)
    return dict(sentence_max_len=sen_max_len,
                sentence_min_len=sen_min_len,
                sentence_average_len=sen_average_len,
                word_max_len=word_max_len,
                word_min_len=word_min_len,
                word_average_len=word_average_len)
