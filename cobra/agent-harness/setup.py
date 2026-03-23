from setuptools import setup
setup(
    name='cli-anything-cobra',
    version='1.0.0',
    packages=['cli_anything.cobra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cobra=cli_anything.cobra:cli']},
)
