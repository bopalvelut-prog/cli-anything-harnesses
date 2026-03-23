from setuptools import setup
setup(
    name='cli-anything-taipy',
    version='1.0.0',
    packages=['cli_anything.taipy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-taipy=cli_anything.taipy:cli']},
)
