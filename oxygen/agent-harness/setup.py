from setuptools import setup
setup(
    name='cli-anything-oxygen',
    version='1.0.0',
    packages=['cli_anything.oxygen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oxygen=cli_anything.oxygen:cli']},
)
