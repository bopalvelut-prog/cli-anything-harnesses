from setuptools import setup
setup(
    name='cli-anything-parking',
    version='1.0.0',
    packages=['cli_anything.parking'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-parking=cli_anything.parking:cli']},
)
