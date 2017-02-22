try:
    # for python 3
    from http.client import responses
except ImportError: # python 2.5 to 2.7
    try:
        from httplib import responses #NOQA
    except ImportError: # for python 2.4
        from BaseHTTPServer import  baseHTTPRequestHandler as _BHRH
        responses = dict([(k,v [0]) for k,v in _BHRH.responses.items()])


