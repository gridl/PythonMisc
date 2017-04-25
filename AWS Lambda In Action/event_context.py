# event is the way to send input paramters for your function
# context is used by the service to describe the execution environment and how the event is recieved and processed


def lambda_handler(event ,context):
    results = event['value1'] + event['value2']
    print(event['message'])
    return results

