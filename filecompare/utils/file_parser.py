# file_parser.py
#
# This module is part of FileCompare and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php

"""FileParser class helps reading properties, xml, ymal, etc."""

import logging

class FileParser():
    """FileParser class helps reading properties, xml, ymal, etc."""

    # Create child logger
    logger = logging.getLogger('FileCompare' + __name__)

    def __int__(self):
        # Create child logger
        self.logger = logging.getLogger('FileCompare' + __name__)