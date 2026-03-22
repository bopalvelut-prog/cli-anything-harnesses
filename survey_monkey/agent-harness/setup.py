from setuptools import setup
setup(
    name='cli-anything-survey_monkey',
    version='1.0.0',
    packages=['cli_anything.survey_monkey'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-survey_monkey=cli_anything.survey_monkey:cli']},
)
