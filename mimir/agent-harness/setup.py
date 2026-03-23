from setuptools import setup
setup(
    name='cli-anything-mimir',
    version='1.0.0',
    packages=['cli_anything.mimir'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mimir=cli_anything.mimir:cli']},
)
