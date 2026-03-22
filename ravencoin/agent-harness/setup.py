from setuptools import setup
setup(
    name='cli-anything-ravencoin',
    version='1.0.0',
    packages=['cli_anything.ravencoin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ravencoin=cli_anything.ravencoin:cli']},
)
