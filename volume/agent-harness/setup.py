from setuptools import setup
setup(
    name='cli-anything-volume',
    version='1.0.0',
    packages=['cli_anything.volume'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-volume=cli_anything.volume:cli']},
)
