from setuptools import setup
setup(
    name='cli-anything-yara',
    version='1.0.0',
    packages=['cli_anything.yara'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yara=cli_anything.yara:cli']},
)
