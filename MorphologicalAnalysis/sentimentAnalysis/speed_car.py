import csv
from slack import slack
from files import get_csv_files_by_dir,generate_path,get_md_files_by_dir,read_markdown_file


def speed_car():
    dir_name = 'speed_car_10_10_10_16'
    file_names = get_csv_files_by_dir(dir_name)
    results = {}
    print(file_names)
    for file in file_names:
        if 'Jira2' in file:
            _jira = jira(dir_name, file)
            results['Jira2'] = _jira
        elif 'Jira' in file:
            _jira = jira(dir_name, file)
            results['Jira'] = _jira
        elif 'ふりかえり：speed car' in file:
            _retro = retro(dir_name, file)
            results['retro'] = _retro
    file_names = get_md_files_by_dir(dir_name)
    for file in file_names:
        if 'Notion' in file:
            _notion = notion(dir_name, file)
            results['notion'] = _notion
    _slack = slack(generate_path(dir_name+'/中鉢PT2023 Slack export Oct 10 2023 - Oct 16 2023',''))
    results['slack'] = _slack
    return results

# [{'Content': 'もっとPRを細かく', 'Created by': 'Jabelic'}]
def retro(dir_name, file_name):
    if not 'ふりかえり：speed car' in file_name: return
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
            # print(item.keys())
            summary = item['Summary']
            reporter = item['Reporter']
            description = item['Description']
            comment = item['Comment1']
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