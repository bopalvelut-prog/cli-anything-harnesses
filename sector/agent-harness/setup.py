from setuptools import setup
setup(
    name='cli-anything-sector',
    version='1.0.0',
    packages=['cli_anything.sector'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sector=cli_anything.sector:cli']},
)
