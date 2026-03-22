from setuptools import setup
setup(
    name='cli-anything-rocketpool',
    version='1.0.0',
    packages=['cli_anything.rocketpool'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rocketpool=cli_anything.rocketpool:cli']},
)
