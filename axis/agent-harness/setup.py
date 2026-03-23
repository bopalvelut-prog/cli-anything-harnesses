from setuptools import setup
setup(
    name='cli-anything-axis',
    version='1.0.0',
    packages=['cli_anything.axis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-axis=cli_anything.axis:cli']},
)
