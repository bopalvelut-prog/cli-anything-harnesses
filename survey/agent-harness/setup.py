from setuptools import setup
setup(
    name='cli-anything-survey',
    version='1.0.0',
    packages=['cli_anything.survey'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-survey=cli_anything.survey:cli']},
)
