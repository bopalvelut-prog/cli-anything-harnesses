from setuptools import setup
setup(
    name='cli-anything-consider',
    version='1.0.0',
    packages=['cli_anything.consider'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-consider=cli_anything.consider:cli']},
)
