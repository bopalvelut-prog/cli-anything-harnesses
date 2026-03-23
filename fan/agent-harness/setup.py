from setuptools import setup
setup(
    name='cli-anything-fan',
    version='1.0.0',
    packages=['cli_anything.fan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fan=cli_anything.fan:cli']},
)
