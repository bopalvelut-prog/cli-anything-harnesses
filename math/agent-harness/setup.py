from setuptools import setup
setup(
    name='cli-anything-math',
    version='1.0.0',
    packages=['cli_anything.math'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-math=cli_anything.math:cli']},
)
