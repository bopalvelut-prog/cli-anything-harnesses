from setuptools import setup
setup(
    name='cli-anything-read',
    version='1.0.0',
    packages=['cli_anything.read'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-read=cli_anything.read:cli']},
)
