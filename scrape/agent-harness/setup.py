from setuptools import setup
setup(
    name='cli-anything-scrape',
    version='1.0.0',
    packages=['cli_anything.scrape'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scrape=cli_anything.scrape:cli']},
)
