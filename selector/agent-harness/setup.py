from setuptools import setup
setup(
    name='cli-anything-selector',
    version='1.0.0',
    packages=['cli_anything.selector'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-selector=cli_anything.selector:cli']},
)
