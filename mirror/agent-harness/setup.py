from setuptools import setup
setup(
    name='cli-anything-mirror',
    version='1.0.0',
    packages=['cli_anything.mirror'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mirror=cli_anything.mirror:cli']},
)
