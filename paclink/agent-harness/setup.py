from setuptools import setup
setup(
    name='cli-anything-paclink',
    version='1.0.0',
    packages=['cli_anything.paclink'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paclink=cli_anything.paclink:cli']},
)
