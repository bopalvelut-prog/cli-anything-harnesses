from setuptools import setup
setup(
    name='cli-anything-runc',
    version='1.0.0',
    packages=['cli_anything.runc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-runc=cli_anything.runc:cli']},
)
