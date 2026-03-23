from setuptools import setup
setup(
    name='cli-anything-pytest',
    version='1.0.0',
    packages=['cli_anything.pytest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pytest=cli_anything.pytest:cli']},
)
