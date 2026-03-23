from setuptools import setup
setup(
    name='cli-anything-speed',
    version='1.0.0',
    packages=['cli_anything.speed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-speed=cli_anything.speed:cli']},
)
