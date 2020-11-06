from song_analyzer.song_parts.song import Song


def count_words_with_pos_tags(song_obj, pos_tags: list) -> int: # TODO - try to get rid of it????????
    """
    Count the number of words in the song with one of the given POS tags
    :param song_obj: Song object
    :param pos_tags: POS tags to search songs with
    :return: number of words with POS tags
    """
    count = 0
    for sentence in song_obj.sentences:
        for word in sentence.words:
            if word.pos in pos_tags:
                count += 1
    return count


def get_words_with_pos_tags(song_obj, pos_tags: list) -> list: # FIXME to set????????????
    """
    Get words with on of the given POS tags
    :param song_obj: Song object
    :param pos_tags: POS tags to search songs with
    :return:
    """
    words = []
    for sentence in song_obj.sentences:
        for word in sentence.words:
            if word.pos in pos_tags:
                words.append(word.data)
    return set(words)


def get_sentence_length_stats(song_obj) -> dict[str, int]:
    """
    Get statistics about the min/max/average length of the sentences in the song
    :return: sentences statistics
    """

    pass


def get_word_length_stats(song_obj) -> dict[str, int]:
    """
    Get statistics about the min/max/average length of the words in the song
    :return: words statistics
    """
    pass

# FIXME - should i set the nouns and adjectives, remove duplicates???? should they be unique?
# FIXME - should i leagel??