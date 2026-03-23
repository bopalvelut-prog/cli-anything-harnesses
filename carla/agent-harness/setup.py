from setuptools import setup
setup(
    name='cli-anything-carla',
    version='1.0.0',
    packages=['cli_anything.carla'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-carla=cli_anything.carla:cli']},
)
