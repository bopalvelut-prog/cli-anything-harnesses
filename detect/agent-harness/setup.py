from setuptools import setup
setup(
    name='cli-anything-detect',
    version='1.0.0',
    packages=['cli_anything.detect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-detect=cli_anything.detect:cli']},
)
