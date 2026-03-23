from setuptools import setup
setup(
    name='cli-anything-road',
    version='1.0.0',
    packages=['cli_anything.road'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-road=cli_anything.road:cli']},
)
