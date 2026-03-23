from setuptools import setup
setup(
    name='cli-anything-ground',
    version='1.0.0',
    packages=['cli_anything.ground'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ground=cli_anything.ground:cli']},
)
