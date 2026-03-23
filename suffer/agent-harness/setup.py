from setuptools import setup
setup(
    name='cli-anything-suffer',
    version='1.0.0',
    packages=['cli_anything.suffer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suffer=cli_anything.suffer:cli']},
)
