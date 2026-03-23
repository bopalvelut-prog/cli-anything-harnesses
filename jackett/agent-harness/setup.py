from setuptools import setup
setup(
    name='cli-anything-jackett',
    version='1.0.0',
    packages=['cli_anything.jackett'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jackett=cli_anything.jackett:cli']},
)
