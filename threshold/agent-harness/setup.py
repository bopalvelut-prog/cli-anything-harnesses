from setuptools import setup
setup(
    name='cli-anything-threshold',
    version='1.0.0',
    packages=['cli_anything.threshold'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-threshold=cli_anything.threshold:cli']},
)
