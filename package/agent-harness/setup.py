from setuptools import setup
setup(
    name='cli-anything-package',
    version='1.0.0',
    packages=['cli_anything.package'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-package=cli_anything.package:cli']},
)
