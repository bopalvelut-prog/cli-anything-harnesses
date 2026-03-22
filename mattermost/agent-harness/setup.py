from setuptools import setup
setup(
    name='cli-anything-mattermost',
    version='1.0.0',
    packages=['cli_anything.mattermost'],
    install_requires=['click', 'requests'],
    entry_points={'console_scripts': ['cli-anything-mattermost=cli_anything.mattermost:cli']},
)
