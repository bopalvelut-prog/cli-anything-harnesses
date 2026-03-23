from setuptools import setup
setup(
    name='cli-anything-mist',
    version='1.0.0',
    packages=['cli_anything.mist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mist=cli_anything.mist:cli']},
)
