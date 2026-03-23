from setuptools import setup
setup(
    name='cli-anything-recall',
    version='1.0.0',
    packages=['cli_anything.recall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recall=cli_anything.recall:cli']},
)
