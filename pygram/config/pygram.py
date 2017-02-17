import os

from pygram.config import BaseConfig
from pygram.utils.const import ABSPATH_DATA
from pygram.filters import grayscale, sepia, nss, brannan, clarendon, inkwell

class PyGramConfig(BaseConfig):
    NAME                = 'PyGram'
    VERSION             = '0.1.0'
    WINDOW_ASPECT_RATIO = 3 / 2
    WINDOW_WIDTH        = 320
    WINDOW_HEIGHT       = int(WINDOW_ASPECT_RATIO * WINDOW_WIDTH)

    ACCEPTED_FILES      = [ ]
    DEFAULT_FILE        = os.path.join(ABSPATH_DATA, 'lenna.png')

    FILTERS             = [
        {
            'name': 'normal',
            'command': lambda image: image
        },
        {
            'name': 'grayscale',
            'command': grayscale
        },
        {
            'name': 'sepia',
            'command': sepia
        },
        {
            'name': '1977',
            'command': nss
        },
        {
            'name': 'brannan',
            'command': brannan
        },
        {
            'name': 'clarendon',
            'command': clarendon
        },
        {
            'name': 'inkwell',
            'command': inkwell
        }
    ]

    BTNGRID_COLS        = 3
    BTNGRID_ROWS        = len(FILTERS) // BTNGRID_COLS + 1
