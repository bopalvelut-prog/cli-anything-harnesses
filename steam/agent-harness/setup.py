from setuptools import setup
setup(
    name='cli-anything-steam',
    version='1.0.0',
    packages=['cli_anything.steam'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-steam=cli_anything.steam:cli']},
)
