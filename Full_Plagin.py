import getpass

from Utils import issue_link, mass_arch, search_issue, generic_token, set_role

while True:
    x = int(input("Привет, для работы, тебе потребуется JQL запрос, и логин и пароль сервисной уз!\n"
                  "1 - Массово связать дочерние запросы, с родительским\n"
                  "2 - Массово заархивировать запросы\n"
                  "3 - Массово добавить во все проекты роль\n"
                  "0 - Выйти\n"))

    match x:
        case 1:
            jql = input("Укажи JQL запрос: ")
            login = str(input("Укажи Логин: "))
            password = getpass.getpass()
            url = input("Укажи ссылку(https://domain.com): ")
            tok = generic_token.create_token(login, password)
            search_issue.get_issues(tok, url, jql)

            fkey = input("Укажи родительский ключ задачи: ")
            issue_link.link(url, tok, fkey)
        case 2:
            jql = input("Укажи JQL запрос: ")
            login = str(input("Укажи Логин: "))
            password = getpass.getpass()
            url = input("Укажи ссылку(https://domain.com): ")
            tok = generic_token.create_token(login, password)
            search_issue.get_issues(tok, url, jql)

            y = int(input("Ты уверен что хочешь заархивировать все запросы?\n0 = Да\n1 = Нет\n"))
            print('ok') if y > 0 else mass_arch.arch(tok, url)

        case 3:
            login = str(input("Укажи Логин: "))
            password = getpass.getpass()
            url = input("Укажи ссылку(https://domain.com): ")
            rle = str(input("Укажите наименование роли: "))
            grp = str(input("Укажите группу которую добавить: "))
            tok = generic_token.create_token(login, password)

            set_role.set_role(tok, url, grp, rle)
        case _:
            break
