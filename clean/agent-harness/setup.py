from setuptools import setup
setup(
    name='cli-anything-clean',
    version='1.0.0',
    packages=['cli_anything.clean'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clean=cli_anything.clean:cli']},
)
