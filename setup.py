import setuptools

with open('README.md', 'r', encoding = 'utf-8') as file:
    long_description = file.read()

__version__ = '0.0.0'

Author_name ='dipan97-hue'
Repo_name = 'End-to-End-Machine-Learning-Project-with-MLFLOW'
Src_Repo ='ML-Project'

setuptools.setup(
    name = Repo_name,
    version = __version__,
    author = Author_name,
    description = 'A small python package for End-to-End Machine Learning Project with MLFLOW',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = f'https://github.com/{Author_name}/{Repo_name}',
    project_urls ={
        'Bug Tracker': f'https://github.com/{Author_name}/{Repo_name}/issues'
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where ='src')

)

