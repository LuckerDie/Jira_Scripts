import requests
import urllib3
import os

urllib3.disable_warnings()


def arch(tokens, urls):
    headers = {
        'Authorization': f'Basic {tokens}',
        'Content-Type': 'application/json',
    }

    with open("issue_id.txt", "r") as f:
        for lis in f.read().splitlines():
            url = f"{urls}/rest/api/2/issue/{lis}/archive"
            requests.put(url, verify=False, headers=headers)
        print("Запросы заархивированы")

    os.remove("issue_id.txt")
