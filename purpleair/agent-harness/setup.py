from setuptools import setup
setup(
    name='cli-anything-purpleair',
    version='1.0.0',
    packages=['cli_anything.purpleair'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-purpleair=cli_anything.purpleair:cli']},
)
