from setuptools import setup
setup(
    name='cli-anything-flag',
    version='1.0.0',
    packages=['cli_anything.flag'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flag=cli_anything.flag:cli']},
)
