from setuptools import setup
setup(
    name='cli-anything-count',
    version='1.0.0',
    packages=['cli_anything.count'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-count=cli_anything.count:cli']},
)
