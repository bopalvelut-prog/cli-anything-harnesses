from setuptools import setup
setup(
    name='cli-anything-lts',
    version='1.0.0',
    packages=['cli_anything.lts'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lts=cli_anything.lts:cli']},
)
