from setuptools import setup
setup(
    name='cli-anything-farm',
    version='1.0.0',
    packages=['cli_anything.farm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-farm=cli_anything.farm:cli']},
)
