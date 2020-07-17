from get_bitbucket_webhook_body import get_bitbucket_webhook_body
import json


if __name__ == "__main__":
    with open('examples/example.json', 'r') as json_file:
        payload = json.load(json_file)
        print(get_bitbucket_webhook_body(payload))
