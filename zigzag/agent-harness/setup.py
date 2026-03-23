from setuptools import setup
setup(
    name='cli-anything-zigzag',
    version='1.0.0',
    packages=['cli_anything.zigzag'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zigzag=cli_anything.zigzag:cli']},
)
