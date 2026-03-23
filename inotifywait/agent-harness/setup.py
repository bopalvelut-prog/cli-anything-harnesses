from setuptools import setup
setup(
    name='cli-anything-inotifywait',
    version='1.0.0',
    packages=['cli_anything.inotifywait'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inotifywait=cli_anything.inotifywait:cli']},
)
