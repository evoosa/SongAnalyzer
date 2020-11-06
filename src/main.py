from song_analyzer.song_parts.song import Song

if __name__ == '__main__':
    song_path = r"C:\Users\evoosa\Desktop\JobShit\SongAnalyzer\lyrics\charlie_cunningham-force_of_habit.txt"
    s = Song(song_path)
    # print(s.path)
    # print(s.lyrics)
    print(s.metadata)