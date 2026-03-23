from setuptools import setup
setup(
    name='cli-anything-sight',
    version='1.0.0',
    packages=['cli_anything.sight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sight=cli_anything.sight:cli']},
)
