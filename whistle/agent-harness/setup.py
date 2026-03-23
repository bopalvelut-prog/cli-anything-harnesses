from setuptools import setup
setup(
    name='cli-anything-whistle',
    version='1.0.0',
    packages=['cli_anything.whistle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-whistle=cli_anything.whistle:cli']},
)
