from setuptools import setup
setup(
    name='cli-anything-pkgconf',
    version='1.0.0',
    packages=['cli_anything.pkgconf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pkgconf=cli_anything.pkgconf:cli']},
)
