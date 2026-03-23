from setuptools import setup
setup(
    name='cli-anything-perses',
    version='1.0.0',
    packages=['cli_anything.perses'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-perses=cli_anything.perses:cli']},
)
