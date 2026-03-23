from setuptools import setup
setup(
    name='cli-anything-four',
    version='1.0.0',
    packages=['cli_anything.four'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-four=cli_anything.four:cli']},
)
