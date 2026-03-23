from setuptools import setup
setup(
    name='cli-anything-railroad',
    version='1.0.0',
    packages=['cli_anything.railroad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-railroad=cli_anything.railroad:cli']},
)
