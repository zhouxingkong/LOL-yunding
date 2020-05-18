'''

Provided C-style string process methods.

@date 2015-03-22
@author Hong-She Liang <starofrainnight@gmail.com>
'''

import six


def escape(text):
    if six.PY2:
        return text.encode('unicode-escape').replace('"', '\\"').replace("'", "\\'")
    else:
        return text.encode('unicode-escape').decode().replace('"', '\\"').replace("'", "\\'")


def unescape(text):
    return six.b(text).decode('unicode-escape')
