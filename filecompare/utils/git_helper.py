# git_helper.py
#
# This module is part of FileCompare and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php

"""FileParser class helps reading properties, xml, ymal, etc."""

import logging

__author__ = 'Senthil Nayagan'
__copyright__ = 'Copyright 2016, IntensiveCoding'
__credits__ = []
__license__ = 'GPL'
__version__ = '1'
__maintainer__ = 'Senthil Nayagan'
__email__ = 'intensive.coding@gmail.com'
__status__ = "Development"

class GitHelper():
    """GitHelper class helps working with Git SCM"""

    # Create child logger
    logger = logging.getLogger('FileCompare.' + __name__)

    def __init__(self):
        """GitHelper initializer"""
        # Create child logger
        self.logger = logging.getLogger('GitHelper.' + __name__)

        self.logger.info('Initializing GitHelper class...')

    def git_init(self, bare=False):
        """Initialize git repository"""