def find_accounts(search_text):
    if not db_is_available:
        return None

    # return list of account ids
    return db_search(search_text)

accounts = find_accounts('python')
if accounts is None:
    print("Error: DB is not available"
else:
    print("Accounts found: would list them here...")