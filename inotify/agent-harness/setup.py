from setuptools import setup
setup(
    name='cli-anything-inotify',
    version='1.0.0',
    packages=['cli_anything.inotify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inotify=cli_anything.inotify:cli']},
)
