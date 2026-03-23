from setuptools import setup
setup(
    name='cli-anything-fetch',
    version='1.0.0',
    packages=['cli_anything.fetch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fetch=cli_anything.fetch:cli']},
)
