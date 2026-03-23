from setuptools import setup
setup(
    name='cli-anything-parseable',
    version='1.0.0',
    packages=['cli_anything.parseable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-parseable=cli_anything.parseable:cli']},
)
