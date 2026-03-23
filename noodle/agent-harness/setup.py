from setuptools import setup
setup(
    name='cli-anything-noodle',
    version='1.0.0',
    packages=['cli_anything.noodle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-noodle=cli_anything.noodle:cli']},
)
