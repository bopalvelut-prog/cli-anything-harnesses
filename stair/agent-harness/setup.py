from setuptools import setup
setup(
    name='cli-anything-stair',
    version='1.0.0',
    packages=['cli_anything.stair'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stair=cli_anything.stair:cli']},
)
