# Mock module has a function called path that can be used as a function decorator
import urllib.request
from unittest.mock import patch

def read_webpage(url):
    response = urllib.request.urlopen(url)
    return response.read()

@patch('urllib.request.urlopen')
def dummy_reader(mock_obj):
    result = read_webpage('https://www.google.com/')

    mock_obj.assert_called_with('https://www.google.com/')
    print(result)
    # instead of html you get a maagicmock object instead

if __name__ == '__main__':
    dummy_reader()