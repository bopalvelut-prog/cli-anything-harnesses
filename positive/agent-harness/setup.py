from setuptools import setup
setup(
    name='cli-anything-positive',
    version='1.0.0',
    packages=['cli_anything.positive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-positive=cli_anything.positive:cli']},
)
