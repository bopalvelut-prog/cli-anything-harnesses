from setuptools import setup
setup(
    name='cli-anything-victim',
    version='1.0.0',
    packages=['cli_anything.victim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-victim=cli_anything.victim:cli']},
)
