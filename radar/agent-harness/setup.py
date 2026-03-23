from setuptools import setup
setup(
    name='cli-anything-radar',
    version='1.0.0',
    packages=['cli_anything.radar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-radar=cli_anything.radar:cli']},
)
