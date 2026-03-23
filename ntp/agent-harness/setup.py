from setuptools import setup
setup(
    name='cli-anything-ntp',
    version='1.0.0',
    packages=['cli_anything.ntp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ntp=cli_anything.ntp:cli']},
)
