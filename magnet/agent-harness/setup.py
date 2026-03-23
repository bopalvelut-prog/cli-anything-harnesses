from setuptools import setup
setup(
    name='cli-anything-magnet',
    version='1.0.0',
    packages=['cli_anything.magnet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-magnet=cli_anything.magnet:cli']},
)
