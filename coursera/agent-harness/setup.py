from setuptools import setup
setup(
    name='cli-anything-coursera',
    version='1.0.0',
    packages=['cli_anything.coursera'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coursera=cli_anything.coursera:cli']},
)
