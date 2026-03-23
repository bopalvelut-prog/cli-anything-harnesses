from setuptools import setup
setup(
    name='cli-anything-signature',
    version='1.0.0',
    packages=['cli_anything.signature'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-signature=cli_anything.signature:cli']},
)
