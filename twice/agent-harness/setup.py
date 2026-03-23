from setuptools import setup
setup(
    name='cli-anything-twice',
    version='1.0.0',
    packages=['cli_anything.twice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-twice=cli_anything.twice:cli']},
)
