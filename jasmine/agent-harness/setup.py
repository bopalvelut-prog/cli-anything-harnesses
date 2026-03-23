from setuptools import setup
setup(
    name='cli-anything-jasmine',
    version='1.0.0',
    packages=['cli_anything.jasmine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jasmine=cli_anything.jasmine:cli']},
)
