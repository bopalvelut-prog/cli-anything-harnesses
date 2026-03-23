from setuptools import setup
setup(
    name='cli-anything-cold',
    version='1.0.0',
    packages=['cli_anything.cold'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cold=cli_anything.cold:cli']},
)
