import os
from datetime import datetime

BASE_DIR = "/".join(os.path.dirname(os.path.realpath(__file__)).split("/")[0:-2])
NOW = datetime.now().strftime("%d-%m-%Y-%H-%M")
LYRICS_DIR = os.path.join(BASE_DIR, 'lyrics')
LYRICS_FILE_PATHS = [os.path.join(LYRICS_DIR, path) for path in os.listdir(LYRICS_DIR)]
SCRIPT_OUTPUTS_DIR = os.path.join(BASE_DIR, 'script_outputs')

HISTOGRAM_PLOT_FILENAME = NOW + '-' + 'histogram.png'
GEN_STATS_FILENAME = NOW + '-' + 'general_statistics.csv'
POS_STATS_FILENAME = NOW + '-' + 'pos_statistics.txt'

CSV_COLUMNS = ['sentence_max_len',
               'sentence_min_len',
               'sentence_average_len',
               'word_max_len',
               'word_min_len',
               'word_average_len']
