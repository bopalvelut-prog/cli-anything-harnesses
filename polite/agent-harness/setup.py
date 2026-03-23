from setuptools import setup
setup(
    name='cli-anything-polite',
    version='1.0.0',
    packages=['cli_anything.polite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-polite=cli_anything.polite:cli']},
)
