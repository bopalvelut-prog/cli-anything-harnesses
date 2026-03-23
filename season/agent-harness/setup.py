from setuptools import setup
setup(
    name='cli-anything-season',
    version='1.0.0',
    packages=['cli_anything.season'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-season=cli_anything.season:cli']},
)
