from setuptools import setup
setup(
    name='cli-anything-make',
    version='1.0.0',
    packages=['cli_anything.make'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-make=cli_anything.make:cli']},
)
