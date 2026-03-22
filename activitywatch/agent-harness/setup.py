from setuptools import setup
setup(
    name='cli-anything-activitywatch',
    version='1.0.0',
    packages=['cli_anything.activitywatch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-activitywatch=cli_anything.activitywatch:cli']},
)
