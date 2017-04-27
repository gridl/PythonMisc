import json
print('Loading function')

def lambda_handler(event, context):
    # TODO implement
    print('Recieved event: ' + json.dumps(event, indent=2))
    if 'name' in event:
        name = event['name']
    else:
        name = 'World'
    greetings = "Hello " + name + '!'
    print(greetings)
    return 'Hello from Lambda'