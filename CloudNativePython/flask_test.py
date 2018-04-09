from CloudNativePython import tweets
import unittest


#test the app and initialoze self.app
class FlaskappTests(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = tweets.test_client()
        # propogate the exceptions to the test client
        self.app.testing = True


def test_user_status_code(self):
    # sends HTTP GET request to the application
    result = self.app.get('/api/v1/users')
    # assert the status code of the response
    self.assertEqual(result.status_code,200)

def test_tweets_test_status_code(self):
    # sends HTTP GET request to the application
    result = self.app.get('/api/v2/tweets')
    # assert the status code of the response
    self.assertEqual(result.status_code, 200)