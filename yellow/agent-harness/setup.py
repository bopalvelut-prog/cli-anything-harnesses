from setuptools import setup
setup(
    name='cli-anything-yellow',
    version='1.0.0',
    packages=['cli_anything.yellow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yellow=cli_anything.yellow:cli']},
)
