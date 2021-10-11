import pathlib

from flucht import app


def get_sections_pages():
    path = pathlib.Path(app.root_path) / 'templates/pages'
    files = [f'pages/{x.name}' for x in path.glob('**/*') if x.is_file()]
    files.sort()
    return files
