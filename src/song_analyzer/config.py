import os

BASE_DIR = r"C:\Users\User\Desktop\PS\SongAnalyzer"
LYRICS_DIR = os.path.join(BASE_DIR, 'lyrics')
LYRICS_FILE_PATHS = [os.path.join(LYRICS_DIR, path) for path in os.listdir(LYRICS_DIR)]
SCRIPT_OUTPUTS_DIR = os.path.join(BASE_DIR, 'script_outputs')
CSV_COLUMNS = ['sentence_max_len', 'sentence_min_len', 'sentence_average_len', 'word_max_len',
               'word_min_len', 'word_average_len']
HISTOGRAM_PLOT_FILENAME = 'histogram.png'
