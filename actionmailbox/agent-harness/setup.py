from setuptools import setup
setup(
    name='cli-anything-actionmailbox',
    version='1.0.0',
    packages=['cli_anything.actionmailbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-actionmailbox=cli_anything.actionmailbox:cli']},
)
