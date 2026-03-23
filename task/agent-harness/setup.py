from setuptools import setup
setup(
    name='cli-anything-task',
    version='1.0.0',
    packages=['cli_anything.task'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-task=cli_anything.task:cli']},
)
