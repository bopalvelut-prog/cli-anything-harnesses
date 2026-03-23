from setuptools import setup
setup(
    name='cli-anything-people',
    version='1.0.0',
    packages=['cli_anything.people'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-people=cli_anything.people:cli']},
)
