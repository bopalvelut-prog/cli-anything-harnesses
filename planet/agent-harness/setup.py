from setuptools import setup
setup(
    name='cli-anything-planet',
    version='1.0.0',
    packages=['cli_anything.planet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-planet=cli_anything.planet:cli']},
)
