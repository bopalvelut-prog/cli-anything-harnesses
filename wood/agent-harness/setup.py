from setuptools import setup
setup(
    name='cli-anything-wood',
    version='1.0.0',
    packages=['cli_anything.wood'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wood=cli_anything.wood:cli']},
)
