from setuptools import setup
setup(
    name='cli-anything-reflect',
    version='1.0.0',
    packages=['cli_anything.reflect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reflect=cli_anything.reflect:cli']},
)
