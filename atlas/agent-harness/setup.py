from setuptools import setup
setup(
    name='cli-anything-atlas',
    version='1.0.0',
    packages=['cli_anything.atlas'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atlas=cli_anything.atlas:cli']},
)
