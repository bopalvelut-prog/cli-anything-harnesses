from setuptools import setup
setup(
    name='cli-anything-mariushernandez',
    version='1.0.0',
    packages=['cli_anything.mariushernandez'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mariushernandez=cli_anything.mariushernandez:cli']},
)
