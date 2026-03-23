from setuptools import setup
setup(
    name='cli-anything-daisy',
    version='1.0.0',
    packages=['cli_anything.daisy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-daisy=cli_anything.daisy:cli']},
)
