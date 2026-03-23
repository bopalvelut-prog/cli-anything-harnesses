from setuptools import setup
setup(
    name='cli-anything-phrase',
    version='1.0.0',
    packages=['cli_anything.phrase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phrase=cli_anything.phrase:cli']},
)
