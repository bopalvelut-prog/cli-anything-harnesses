from setuptools import setup
setup(
    name='cli-anything-safe',
    version='1.0.0',
    packages=['cli_anything.safe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-safe=cli_anything.safe:cli']},
)
