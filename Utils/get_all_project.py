import requests
import json
import urllib3

urllib3.disable_warnings()


def get_project(tokens, urls):
    headers = {
        'Authorization': f'Basic {tokens}',
        'Content-Type': 'application/json',
    }

    with open("data_file.json", "w") as new_file:
        resp = requests.get(url=urls + '/rest/api/latest/project', headers=headers, verify=False)
        ds = {'projects': resp.json()}
        json.dump(ds, new_file, ensure_ascii=False, indent=4)
        new_file.close()
