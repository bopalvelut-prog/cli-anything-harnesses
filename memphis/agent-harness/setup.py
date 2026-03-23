from setuptools import setup
setup(
    name='cli-anything-memphis',
    version='1.0.0',
    packages=['cli_anything.memphis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-memphis=cli_anything.memphis:cli']},
)
