from setuptools import setup
setup(
    name='cli-anything-anchore',
    version='1.0.0',
    packages=['cli_anything.anchore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anchore=cli_anything.anchore:cli']},
)
