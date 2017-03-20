# MOCK (IN UNITTEST)
# replace parts of your system under test with mock objects and make assertions about how they ahve been used

from unittest.mock import MagicMock
instance = ProductionClass()
instance.method = MagicMock(return_value=3) # magic mock will always return the value 3 when called, counts the number of method calls it recieves, records the signature it was called with and contains asseriton methods
instance.method(3,4,5,key='value')
instance.method.assert_called_with(3,4,5, key='value')

import unittest.mock as mock

def mock_search(self):
    class MockSearchQeurySet(SearchQuerySet):
        def __iter__(self):
            return iter(['foo','boo','baz'])

    return MockSearchQuerySet()


#Searchform here refers to the imported class reference
#myapp.SearchForm, and modifies this instance not the code where the searchform class itself is initially defined
@mock.path("myapp.SearchForm.seach",mock_search)
def test_new_watchilist_activities(self):
    # get_search_results runs a search and iterates over the result
    self.assertEqual(len(myapp.get_search_results(q="fish")),3)



