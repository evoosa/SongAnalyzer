from song_analyzer.song_parts.song import Song

def get_song_pos_entities(lyrics_path: str) -> dict:
    """
    Get POS entities data for a given song
    :param lyrics_path: path to the lyrics file
    :return: POS entities for the song
    """
    song_obj = Song(lyrics_path)
    nouns = get_words_with_pos_tags(song_obj.sentences, ['NN', 'NNS', 'NNP', 'NNPS'])
    adjectives = get_words_with_pos_tags(song_obj.sentences, ['JJ', 'JJR', 'JJS'])
    noun_to_adj_ratio = len(nouns) / len(adjectives)
    return dict(
        nouns=nouns,
        adjectives=adjectives,
        noun_to_adjective_ratio=noun_to_adj_ratio
    )


def get_song_length_stats(lyrics_path: str) -> dict[str, int]:
    """
    Get statistics about the min/max/average length of the sentences and words in the song
    :param lyrics_path: path to the lyrics file
    :return: length stats for the song
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


def get_words_with_pos_tags(sentences, pos_tags: list) -> list:
    """
    Get words with on of the given POS tags
    :param self: Song object
    :param pos_tags: POS tags to search songs with
    :return:
    """
    words = []
    for sentence in sentences:
        for word in sentence.words:
            if word.pos in pos_tags:
                words.append(word.data)
    return words
