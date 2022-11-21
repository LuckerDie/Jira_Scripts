import requests
import json
import urllib3

urllib3.disable_warnings()


def link(urls, tokens, fath_key):
    url = urls + "/rest/api/latest/issueLink"
    file = open("issue_id.txt", "r")

    lines = file.read().splitlines()

    headers = {
        'Authorization': f'Basic {tokens}',
        'Content-Type': 'application/json',
    }

    for lis in lines:
        payload = json.dumps({
            "type": {
                "name": "Blocks"
            },
            "inwardIssue": {
                "key": f"{fath_key}"
            },
            "outwardIssue": {
                "key": lis
            }
        })
        requests.request("POST", url, verify=False, headers=headers, data=payload)

    print("Запросы привязаны.")

