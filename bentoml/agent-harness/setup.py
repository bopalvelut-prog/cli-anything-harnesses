from setuptools import setup
setup(
    name='cli-anything-bentoml',
    version='1.0.0',
    packages=['cli_anything.bentoml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bentoml=cli_anything.bentoml:cli']},
)
