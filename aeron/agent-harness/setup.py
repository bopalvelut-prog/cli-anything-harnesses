from setuptools import setup
setup(
    name='cli-anything-aeron',
    version='1.0.0',
    packages=['cli_anything.aeron'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aeron=cli_anything.aeron:cli']},
)
