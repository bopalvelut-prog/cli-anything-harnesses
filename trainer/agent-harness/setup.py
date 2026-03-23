from setuptools import setup
setup(
    name='cli-anything-trainer',
    version='1.0.0',
    packages=['cli_anything.trainer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trainer=cli_anything.trainer:cli']},
)
