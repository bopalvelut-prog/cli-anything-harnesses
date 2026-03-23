from setuptools import setup
setup(
    name='cli-anything-independent',
    version='1.0.0',
    packages=['cli_anything.independent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-independent=cli_anything.independent:cli']},
)
