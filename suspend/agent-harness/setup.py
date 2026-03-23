from setuptools import setup
setup(
    name='cli-anything-suspend',
    version='1.0.0',
    packages=['cli_anything.suspend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suspend=cli_anything.suspend:cli']},
)
