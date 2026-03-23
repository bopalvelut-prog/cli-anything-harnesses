from setuptools import setup
setup(
    name='cli-anything-pyenv',
    version='1.0.0',
    packages=['cli_anything.pyenv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyenv=cli_anything.pyenv:cli']},
)
