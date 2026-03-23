from setuptools import setup
setup(
    name='cli-anything-vscode_server',
    version='1.0.0',
    packages=['cli_anything.vscode_server'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vscode_server=cli_anything.vscode_server:cli']},
)
