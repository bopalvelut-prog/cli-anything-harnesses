from setuptools import setup
setup(
    name='cli-anything-pocket',
    version='1.0.0',
    packages=['cli_anything.pocket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pocket=cli_anything.pocket:cli']},
)
