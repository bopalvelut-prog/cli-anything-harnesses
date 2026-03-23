from setuptools import setup
setup(
    name='cli-anything-cactus',
    version='1.0.0',
    packages=['cli_anything.cactus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cactus=cli_anything.cactus:cli']},
)
