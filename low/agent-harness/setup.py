from setuptools import setup
setup(
    name='cli-anything-low',
    version='1.0.0',
    packages=['cli_anything.low'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-low=cli_anything.low:cli']},
)
