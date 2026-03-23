from setuptools import setup
setup(
    name='cli-anything-kazoo',
    version='1.0.0',
    packages=['cli_anything.kazoo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kazoo=cli_anything.kazoo:cli']},
)
