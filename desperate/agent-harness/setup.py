from setuptools import setup
setup(
    name='cli-anything-desperate',
    version='1.0.0',
    packages=['cli_anything.desperate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-desperate=cli_anything.desperate:cli']},
)
