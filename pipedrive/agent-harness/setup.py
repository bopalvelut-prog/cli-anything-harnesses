from setuptools import setup
setup(
    name='cli-anything-pipedrive',
    version='1.0.0',
    packages=['cli_anything.pipedrive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pipedrive=cli_anything.pipedrive:cli']},
)
