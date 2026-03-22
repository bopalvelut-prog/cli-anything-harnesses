from setuptools import setup
setup(
    name='cli-anything-braco42',
    version='1.0.0',
    packages=['cli_anything.braco42'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco42=cli_anything.braco42:cli']},
)
