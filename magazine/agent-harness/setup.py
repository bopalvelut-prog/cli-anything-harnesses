from setuptools import setup
setup(
    name='cli-anything-magazine',
    version='1.0.0',
    packages=['cli_anything.magazine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-magazine=cli_anything.magazine:cli']},
)
