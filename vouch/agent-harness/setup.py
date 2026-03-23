from setuptools import setup
setup(
    name='cli-anything-vouch',
    version='1.0.0',
    packages=['cli_anything.vouch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vouch=cli_anything.vouch:cli']},
)
