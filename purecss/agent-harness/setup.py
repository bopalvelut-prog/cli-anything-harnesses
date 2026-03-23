from setuptools import setup
setup(
    name='cli-anything-purecss',
    version='1.0.0',
    packages=['cli_anything.purecss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-purecss=cli_anything.purecss:cli']},
)
