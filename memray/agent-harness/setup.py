from setuptools import setup
setup(
    name='cli-anything-memray',
    version='1.0.0',
    packages=['cli_anything.memray'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-memray=cli_anything.memray:cli']},
)
