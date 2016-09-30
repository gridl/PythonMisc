#dictionary that acts as DB storage
MOCK_USERS = {'test@example.com': '123456'}

class MockDBHelper:
    # check if a user exists in our database and return the password if it does
    def get_user(self,email):
        if email in MOCK_USERS:
            return MOCK_USERS[email]
        return None