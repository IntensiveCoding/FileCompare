# file_parser.py
#
# This module is part of FileCompare and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php

"""FileParser class helps reading properties, xml, ymal, etc."""

import logging
from configparser import ConfigParser
import codecs

class FileParser():
    """FileParser class helps reading properties, xml, ymal, etc."""

    # Create child logger
    logger = logging.getLogger('FileCompare.' + __name__)

    def __init__(self):
        """FileParser initializer"""
        # Create child logger
        self.logger = logging.getLogger('FileCompare.' + __name__)

        self.logger.info('Initializing FileParser class...')

        parser = ConfigParser()

        # Open file with the correct encoding
        with codecs.open('../resources/config.properties', 'r', encoding='utf-8') as propFile:
            parser.read_file(propFile)

        self.git_url = parser.get('git', 'url')

        self.logger.debug('Git URL: {url}'.format(url=self.git_url))
