from setuptools import setup
setup(
    name='cli-anything-broad',
    version='1.0.0',
    packages=['cli_anything.broad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-broad=cli_anything.broad:cli']},
)
