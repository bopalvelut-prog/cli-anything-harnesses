from setuptools import setup
setup(
    name='cli-anything-onedrive',
    version='1.0.0',
    packages=['cli_anything.onedrive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-onedrive=cli_anything.onedrive:cli']},
)
