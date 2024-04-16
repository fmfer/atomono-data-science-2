import csv
from slack import slack
from files import get_csv_files_by_dir,generate_path,read_markdown_file,get_md_files_by_dir,get_json_files

FIGJAM_ELEPHANT_FISH_FILE_NAME = '振り返り　象、死んだ魚、嘔吐 (11月分)'

def elephant_fish():
    dir_name = 'elephant_fish_10_31_11_06'
    results = {}

    file_names = get_csv_files_by_dir(dir_name)
    for file in file_names:
        if 'Jira (1)' in file:
            _jira = jira(dir_name, file)
            results['Jira (1)'] = _jira
        elif 'Jira' in file:
            _jira = jira(dir_name, file)
            results['Jira'] = _jira
        elif FIGJAM_ELEPHANT_FISH_FILE_NAME in file:
            _retro = retro(dir_name, file)
            results['retro'] = _retro

    file_names = get_md_files_by_dir(dir_name)
    for file in file_names:
        if 'Notion' in file:
            _notion = notion(dir_name, file)
            results['notion'] = _notion
    _slack = slack(generate_path(dir_name+'/中鉢PT2023 Slack export Oct 31 2023 - Nov 6 2023',''))
    results['slack'] = _slack
    return results

# [{'Content': 'もっとPRを細かく', 'Created by': 'Jabelic'}]
def retro(dir_name, file_name):
    if not FIGJAM_ELEPHANT_FISH_FILE_NAME in file_name: return
    results = []
    with open (
        generate_path(dir_name,file_name),
        'r',
        encoding='utf-8'
    ) as f:
        dict_reader = csv.DictReader(f)
        contents = [row for row in dict_reader]
        for item in contents:
            content = item['Content']
            created_by = item['Created by']
            Dict = {
                'Content': content,
                'Created by': created_by
            }
            results.append(Dict)
    return results


# [{'summary': 'pulldownMenuに編集・削除を組み込む', 'reporter': 'HibikiMizuno', 'description': '', 'comment': ''}]
def jira(dir_name, file_name):
    if not 'Jira' in file_name: return
    with open (
        generate_path(dir_name,file_name),
        'r',
        encoding='utf-8'
    ) as f:
        dict_reader = csv.DictReader(f)
        contents = [row for row in dict_reader]
        result = []
        for item in contents:
            summary = item['Summary']
            reporter = item['Reporter']
            description = item['Description']
            comment = item['Comment']
            Dict = {
                'summary': summary,
                'reporter': reporter,
                'description': description,
                'comment': comment
            }
            result.append(Dict)
        return result


def notion(dir_name, file_name):
    if not 'Notion' in file_name: return
    content = read_markdown_file(generate_path(dir_name,file_name))
    return content
