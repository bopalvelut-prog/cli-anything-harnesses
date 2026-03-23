from setuptools import setup
setup(
    name='cli-anything-reframe',
    version='1.0.0',
    packages=['cli_anything.reframe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reframe=cli_anything.reframe:cli']},
)
