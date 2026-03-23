from setuptools import setup
setup(
    name='cli-anything-sphere',
    version='1.0.0',
    packages=['cli_anything.sphere'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sphere=cli_anything.sphere:cli']},
)
