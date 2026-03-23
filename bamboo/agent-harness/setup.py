from setuptools import setup
setup(
    name='cli-anything-bamboo',
    version='1.0.0',
    packages=['cli_anything.bamboo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bamboo=cli_anything.bamboo:cli']},
)
