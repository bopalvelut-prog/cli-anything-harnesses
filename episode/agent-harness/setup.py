from setuptools import setup
setup(
    name='cli-anything-episode',
    version='1.0.0',
    packages=['cli_anything.episode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-episode=cli_anything.episode:cli']},
)
