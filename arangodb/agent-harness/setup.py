from setuptools import setup
setup(
    name='cli-anything-arangodb',
    version='1.0.0',
    packages=['cli_anything.arangodb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arangodb=cli_anything.arangodb:cli']},
)
