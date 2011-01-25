#!/usr/bin/env python
# (C) Copyright 2010 Brandyn A. White
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Convert packed (filename)\t(b64data)\n to (filename, data)
"""

__author__ = 'Brandyn A. White <bwhite@cs.umd.edu>'
__license__ = 'GPL V3'

import base64
import hadoopy


def mapper(key, value):
    name, data = value.split('\t')
    yield name, base64.b64decode(data)


def reducer(key, values):
    for value in values:
        yield key, value

if __name__ == "__main__":
    if hadoopy.run(mapper, reducer):
        hadoopy.print_doc_quit(__doc__)
