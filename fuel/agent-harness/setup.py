from setuptools import setup
setup(
    name='cli-anything-fuel',
    version='1.0.0',
    packages=['cli_anything.fuel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fuel=cli_anything.fuel:cli']},
)
