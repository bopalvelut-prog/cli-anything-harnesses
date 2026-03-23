from setuptools import setup
setup(
    name='cli-anything-innocent',
    version='1.0.0',
    packages=['cli_anything.innocent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-innocent=cli_anything.innocent:cli']},
)
