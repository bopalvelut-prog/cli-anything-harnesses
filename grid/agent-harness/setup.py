from setuptools import setup
setup(
    name='cli-anything-grid',
    version='1.0.0',
    packages=['cli_anything.grid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grid=cli_anything.grid:cli']},
)
