from setuptools import setup
setup(
    name='cli-anything-situation',
    version='1.0.0',
    packages=['cli_anything.situation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-situation=cli_anything.situation:cli']},
)
