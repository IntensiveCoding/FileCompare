# file_compare.py
#
# This module is part of FileCompare and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php

"""FileCompare is an utility to compare files between
different revisions"""

import argparse
import logging.config
from filecompare.utils.file_parser import FileParser

__author__ = 'Senthil Nayagan'
__copyright__ = 'Copyright 2016, IntensiveCoding'
__credits__ = []
__license__ = 'GPL'
__version__ = '1'
__maintainer__ = 'Senthil Nayagan'
__email__ = 'intensive.coding@gmail.com'
__status__ = "Development"

CONFIG_FILE = '../resources/file_compare'

def main():
    """

    :rtype: object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-file', type=argparse.FileType('r'), help='Specify the config file')

    args = parser.parse_args()

    logging.config.fileConfig('../resources/logging.conf', disable_existing_loggers=False)

    # Create logger
    logger = logging.getLogger('FileCompare')

    if args.config_file:
        cfg_file = args.config_file
    else:
        cfg_file = CONFIG_FILE

    logger.info('FileCompare starts...')

    fileParser = FileParser()
    print(fileParser.git_url)


if __name__ == '__main__':
    main()