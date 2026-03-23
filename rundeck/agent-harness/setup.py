from setuptools import setup
setup(
    name='cli-anything-rundeck',
    version='1.0.0',
    packages=['cli_anything.rundeck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rundeck=cli_anything.rundeck:cli']},
)
