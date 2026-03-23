from setuptools import setup
setup(
    name='cli-anything-term',
    version='1.0.0',
    packages=['cli_anything.term'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-term=cli_anything.term:cli']},
)
