import json
import os

def clean_nb(nb_data):
    cells = nb_data['cells']
    for c in cells:
        c['metadata'] = {}
        c['execution_count'] = None

    nb_data['metadata'] = {'jupytext': {'split_at_heading': True}, 'kernelspec': {'display_name': 'Python 3',
                                                                                  'language': 'python',
                                                                                  'name': 'python3'}}
    return nb_data

def prepend_setup_code(notebook_path, code_path):
    with open(notebook_path, 'r') as f:
        data = json.load(f)

        code = {'cell_type': 'code', 'metadata': {}, 'outputs': [], 'execution_count': None}
        code['source'] = [x+'\n' for x in open(code_path, 'r').read().split('\n')]
        data['cells'].insert(0, code)


    os.makedirs('student_lessons', exist_ok=True)
    with open(f'student_lessons/{os.path.split(notebook_path)[-1]}', 'w+') as f:
        json.dump(clean_nb(data), f)


SETUP_PATH = 'setup_cell'
for x in os.listdir('raw'):
    print(x)
    prepend_setup_code(f'raw/{x}', SETUP_PATH)
