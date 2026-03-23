from setuptools import setup
setup(
    name='cli-anything-threat',
    version='1.0.0',
    packages=['cli_anything.threat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-threat=cli_anything.threat:cli']},
)
