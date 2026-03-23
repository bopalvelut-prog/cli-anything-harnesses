from setuptools import setup
setup(
    name='cli-anything-drone',
    version='1.0.0',
    packages=['cli_anything.drone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drone=cli_anything.drone:cli']},
)
