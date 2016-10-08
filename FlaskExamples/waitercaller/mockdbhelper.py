#dictionary that acts as DB storage
import datetime
MOCK_USERS = [{"email": "test@example.com","salt":"8Fb23mMNHD5Zb8pr2qWA3PE9bH0=", "hashed": "1736f83698df3f8153c1fbd6ce2840f8aace4f200771a46672635374073cc876cf0aa6a31f780e576578f791b5555b50df46303f0c3a7f2d21f91aa1429ac22e"}]
MOCK_TABLES = [{"_id": "1", "number": "1", "owner": "test@example.com","url": "mockurl"}]
MOCK_REQUESTS = [{"_id": "1", "table_number": "1","table_id": "1", "time": datetime.datetime.now()}]
# the preceding global creates a single mock attention request for table number 1 and sets the time of the request to
#  be the time when we started the waitercaller app

class MockDBHelper:
    # check if a user exists in our database and return the password if it does
    def get_user(self,email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({"email": email, "salt":salt,"hashed":hashed})
        # get_user  now needs to loop through all the mock users to find out whether any match the input email


    def add_table(self, number, owner):
        MOCK_TABLES.append({"_id":str(number), "number":number,"owner":owner})
        return number

    def update_table(self, _id, url): # to associate a URL with a table
        for table in MOCK_TABLES:
            if table.get("_id") == _id:
                table["url"] = url
                break

    def get_tables(self, owner_id):
        return MOCK_TABLES


    def delete_table(self,table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get("_id") == table_id:
                del MOCK_TABLES[i]
            break

    def get_requests(self,owner_id):
        return MOCK_REQUESTS

    def delete_request(self, request_id):
        for i, request in enumerate(MOCK_REQUESTS):
            if request.get("_id") == request_id:
                del MOCK_REQUESTS[i]
                break
