from setuptools import setup
setup(
    name='cli-anything-supply',
    version='1.0.0',
    packages=['cli_anything.supply'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-supply=cli_anything.supply:cli']},
)
