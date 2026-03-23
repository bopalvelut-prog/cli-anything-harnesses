from setuptools import setup
setup(
    name='cli-anything-holiday',
    version='1.0.0',
    packages=['cli_anything.holiday'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-holiday=cli_anything.holiday:cli']},
)
