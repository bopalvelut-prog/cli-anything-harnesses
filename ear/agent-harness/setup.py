from setuptools import setup
setup(
    name='cli-anything-ear',
    version='1.0.0',
    packages=['cli_anything.ear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ear=cli_anything.ear:cli']},
)
