from setuptools import setup
setup(
    name='cli-anything-bell',
    version='1.0.0',
    packages=['cli_anything.bell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bell=cli_anything.bell:cli']},
)
