from setuptools import setup
setup(
    name='cli-anything-mpv',
    version='1.0.0',
    packages=['cli_anything.mpv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mpv=cli_anything.mpv:cli']},
)
