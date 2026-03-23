from setuptools import setup
setup(
    name='cli-anything-cups',
    version='1.0.0',
    packages=['cli_anything.cups'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cups=cli_anything.cups:cli']},
)
