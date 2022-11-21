import requests
import json
import urllib3

urllib3.disable_warnings()


def get_issues(tokens, url, jql):
    headers = {
        'Authorization': f'Basic {tokens}',
        'Content-Type': 'application/json'
    }

    to_json = json.dumps({
        "jql": jql,
        'maxResults': 200000,
        'fields': [
            'id'
        ]
    })

    url = f"{url}/rest/api/latest/search"
    r = requests.post(url, headers=headers, data=to_json, verify=False)

    if r.status_code == 200:
        print("I get issue")
        response = r.json()
        with open('issue_id.txt', 'w', encoding='utf-8') as f:
            for issue in response['issues']:
                f.writelines(issue['key'] + "\n")
        f.close()
        print("Запросы получил")
    else:
        print("I don`t get issue")


