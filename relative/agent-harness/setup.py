from setuptools import setup
setup(
    name='cli-anything-relative',
    version='1.0.0',
    packages=['cli_anything.relative'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-relative=cli_anything.relative:cli']},
)
