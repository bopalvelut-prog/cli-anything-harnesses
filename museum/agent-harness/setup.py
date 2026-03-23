from setuptools import setup
setup(
    name='cli-anything-museum',
    version='1.0.0',
    packages=['cli_anything.museum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-museum=cli_anything.museum:cli']},
)
