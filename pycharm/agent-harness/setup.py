from setuptools import setup
setup(
    name='cli-anything-pycharm',
    version='1.0.0',
    packages=['cli_anything.pycharm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pycharm=cli_anything.pycharm:cli']},
)
