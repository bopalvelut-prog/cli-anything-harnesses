from setuptools import setup
setup(
    name='cli-anything-scrap',
    version='1.0.0',
    packages=['cli_anything.scrap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scrap=cli_anything.scrap:cli']},
)
