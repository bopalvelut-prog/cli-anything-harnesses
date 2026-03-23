from setuptools import setup
setup(
    name='cli-anything-remarkable',
    version='1.0.0',
    packages=['cli_anything.remarkable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-remarkable=cli_anything.remarkable:cli']},
)
