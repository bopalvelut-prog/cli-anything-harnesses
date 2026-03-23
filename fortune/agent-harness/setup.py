from setuptools import setup
setup(
    name='cli-anything-fortune',
    version='1.0.0',
    packages=['cli_anything.fortune'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fortune=cli_anything.fortune:cli']},
)
