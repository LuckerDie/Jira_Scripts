import requests
import json
import urllib3
from Utils import get_all_project

urllib3.disable_warnings()


def get_role(tokens, urls, role_name):
    headers = {
        'Authorization': f'Basic {tokens}',
        'Content-Type': 'application/json',
    }

    get_all_project.get_project(tokens, urls)

    with open("data_file.json", "r") as file:
        project_ds = json.load(file)

        for project in project_ds['projects']:
            resp = requests.get(url=urls + f"/rest/api/latest/project/{project['id']}/role", headers=headers,
                                verify=False)
            project['role_id'] = (resp.json()[f'{role_name}'].split('/')[-1])

        with open("data_file.json", "w") as cool_file:
            json.dump(project_ds, cool_file, ensure_ascii=False, indent=4)
