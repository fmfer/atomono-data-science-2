# material/
# ├── KPT_7_26_08_01
# │   ├── 060015e2-66d6-4faf-955a-6b9c55018047_Export-0267666c-3498-434c-a0ab-f01cbc1cc219.zip
# │   ├── Jira (1).csv
# │   ├── Jira.csv
# │   ├── 中鉢PT2023 Channel Analytics Jul 26, 2023 - Aug 1, 2023.csv
# │   ├── 中鉢PT2023 Member Analytics Jul 26, 2023 - Aug 1, 2023.csv
# │   └── 中鉢PT2023 Slack export Jul 26 2023 - Aug 1 2023.zip
# ├── elephant_fish_10_31_11_06
# │   ├── 38557b08-f90b-401d-9f3b-890dd3106167_Export-243dc59b-b77c-41a2-b477-e6eba3ebc415.zip
# │   ├── Jira (1).csv
# │   ├── Jira.csv
# │   ├── 中鉢PT2023 Channel Analytics Oct 31, 2023 - Nov 6, 2023.csv
# │   ├── 中鉢PT2023 Member Analytics Oct 31, 2023 - Nov 6, 2023.csv
# │   ├── 中鉢PT2023 Slack export Oct 31 2023 - Nov 6 2023.zip
# │   └── 振り返り　象、死んだ魚、嘔吐 (11月分).csv
# ├── fun_done_learn_10_24_10_30
# │   ├── Jira (1).csv
# │   ├── Jira.csv
# │   ├── acb09e44-7a43-409c-8d70-ffaa4b904a75_Export-3523b768-d3a3-4114-8c4b-f54599dbe029.zip
# │   ├── fun,done,learn.csv
# │   ├── 中鉢PT2023 Channel Analytics Oct 24, 2023 - Oct 30, 2023.csv
# │   ├── 中鉢PT2023 Member Analytics Oct 24, 2023 - Oct 30, 2023.csv
# │   └── 中鉢PT2023 Slack export Oct 24 2023 - Oct 30 2023.zip
# ├── speed_car_10_10_10_16
# │   ├── Jira (1).csv
# │   ├── Jira.csv
# │   ├── a4cd6bf6-0c86-4ccb-b38f-74c65412b8d9_Export-0536fdc0-638c-4e54-992b-0f1662c41672.zip
# │   ├── ふりかえり：speed car.csv
# │   ├── 中鉢PT2023 Channel Analytics Oct 10, 2023 - Oct 16, 2023.csv
# │   ├── 中鉢PT2023 Member Analytics Oct 10, 2023 - Oct 16, 2023.csv
# │   └── 中鉢PT2023 Slack export Oct 10 2023 - Oct 16 2023.zip
# └── star_fish_10_17_10_23
#     ├── Jira (1).csv
#     ├── Jira.csv
#     ├── c3ab8dfb-65e1-4d10-8bac-e526ae0b2fec_Export-01f47844-0a87-4423-b4c0-d5394ae14c23.zip
#     ├── ふりかえり_ Star Fish.csv
#     ├── 中鉢PT2023 Channel Analytics Oct 17, 2023 - Oct 23, 2023.csv
#     ├── 中鉢PT2023 Member Analytics Oct 17, 2023 - Oct 23, 2023.csv

# ふりかえり
# JIRA
# slack


# dirごとの　csv fileの配列を返す
import os

def get_csv_files(dir):
    csv_files = []
    for file in os.listdir(dir):
        if file.endswith('.csv'):
            csv_files.append(file)
    return csv_files

def get_md_files(dir):
    md_files = []
    for file in os.listdir(dir):
        if file.endswith('.md'):
            md_files.append(file)
    return md_files

def get_json_files(dir):
    json_files = []
    for file in os.listdir(dir):
        if file.endswith('.json'):
            json_files.append(file)
    return json_files

def get_csv_files_by_dir(dir):
    return get_csv_files('../material/' + dir)

def get_md_files_by_dir(dir):
    return get_md_files('../material/' + dir)

def get_json_files_by_dir(dir):
    return get_json_files('../material/' + dir)

def generate_path(dir,file):
    return '../material/' + dir + '/' + file


def read_markdown_file(file_path):
    """
    Read the contents of a markdown file and return its content.

    Parameters:
    file_path (str): The path to the markdown file.

    Returns:
    str: The content of the markdown file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"

