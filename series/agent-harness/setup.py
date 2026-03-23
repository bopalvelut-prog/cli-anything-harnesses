from setuptools import setup
setup(
    name='cli-anything-series',
    version='1.0.0',
    packages=['cli_anything.series'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-series=cli_anything.series:cli']},
)
