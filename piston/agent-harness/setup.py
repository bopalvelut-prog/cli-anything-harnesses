from setuptools import setup
setup(
    name='cli-anything-piston',
    version='1.0.0',
    packages=['cli_anything.piston'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-piston=cli_anything.piston:cli']},
)
