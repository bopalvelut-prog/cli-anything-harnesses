from setuptools import setup
setup(
    name='cli-anything-mpd',
    version='1.0.0',
    packages=['cli_anything.mpd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mpd=cli_anything.mpd:cli']},
)
