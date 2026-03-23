from setuptools import setup
setup(
    name='cli-anything-ptp',
    version='1.0.0',
    packages=['cli_anything.ptp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ptp=cli_anything.ptp:cli']},
)
