from setuptools import setup
setup(
    name='cli-anything-sneakers',
    version='1.0.0',
    packages=['cli_anything.sneakers'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sneakers=cli_anything.sneakers:cli']},
)
