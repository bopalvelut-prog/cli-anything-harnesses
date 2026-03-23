from setuptools import setup
setup(
    name='cli-anything-cliff',
    version='1.0.0',
    packages=['cli_anything.cliff'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cliff=cli_anything.cliff:cli']},
)
