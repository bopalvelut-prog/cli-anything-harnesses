from setuptools import setup
setup(
    name='cli-anything-reality',
    version='1.0.0',
    packages=['cli_anything.reality'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reality=cli_anything.reality:cli']},
)
