from setuptools import setup
setup(
    name='cli-anything-altair',
    version='1.0.0',
    packages=['cli_anything.altair'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-altair=cli_anything.altair:cli']},
)
