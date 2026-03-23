from setuptools import setup
setup(
    name='cli-anything-hyperloglog',
    version='1.0.0',
    packages=['cli_anything.hyperloglog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hyperloglog=cli_anything.hyperloglog:cli']},
)
