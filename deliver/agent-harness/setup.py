from setuptools import setup
setup(
    name='cli-anything-deliver',
    version='1.0.0',
    packages=['cli_anything.deliver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deliver=cli_anything.deliver:cli']},
)
