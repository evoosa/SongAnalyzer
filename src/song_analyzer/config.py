import os
from datetime import datetime

NOW = datetime.now().strftime("%d-%m-%Y-%H-%M")
BASE_DIR = r"/opt/song_analyzer"
LYRICS_DIR = os.path.join(BASE_DIR, 'lyrics')
LYRICS_FILE_PATHS = [os.path.join(LYRICS_DIR, path) for path in os.listdir(LYRICS_DIR)]
SCRIPT_OUTPUTS_DIR = os.path.join(BASE_DIR, 'script_outputs')

HISTOGRAM_PLOT_FILENAME = 'histogram.png'
GEN_STATS_FILENAME = 'general_statistics.csv'
POS_STATS_FILENAME = 'pos_statistics.txt'

CSV_COLUMNS = ['sentence_max_len',
               'sentence_min_len',
               'sentence_average_len',
               'word_max_len',
               'word_min_len',
               'word_average_len']
