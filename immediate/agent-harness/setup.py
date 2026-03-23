from setuptools import setup
setup(
    name='cli-anything-immediate',
    version='1.0.0',
    packages=['cli_anything.immediate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-immediate=cli_anything.immediate:cli']},
)
