from setuptools import setup
setup(
    name='cli-anything-bury',
    version='1.0.0',
    packages=['cli_anything.bury'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bury=cli_anything.bury:cli']},
)
