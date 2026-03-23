from setuptools import setup
setup(
    name='cli-anything-fifth',
    version='1.0.0',
    packages=['cli_anything.fifth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fifth=cli_anything.fifth:cli']},
)
