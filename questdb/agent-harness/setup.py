from setuptools import setup
setup(
    name='cli-anything-questdb',
    version='1.0.0',
    packages=['cli_anything.questdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-questdb=cli_anything.questdb:cli']},
)
