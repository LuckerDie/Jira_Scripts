import json
import os
import requests
import urllib3
from Utils import get_project_role

urllib3.disable_warnings()


def set_role(tokens, urls, groups, role_name):
    headers = {
        'Authorization': f'Basic {tokens}',
        'Content-Type': 'application/json',
    }

    body = {"group": [f"{groups}"]}

    get_project_role.get_role(tokens, urls, role_name)

    with open("data_file.json", 'r') as file:
        project_ds = json.load(file)

        for ids in project_ds['projects']:
            r = requests.post(headers=headers, url=urls + f"/rest/api/latest/project/{ids['id']}/role/{ids['role_id']}",
                              verify=False, data=json.dumps(body))

    os.remove('data_file.json')
    print("Готово!")

