from setuptools import setup
setup(
    name='cli-anything-pages',
    version='1.0.0',
    packages=['cli_anything.pages'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pages=cli_anything.pages:cli']},
)
