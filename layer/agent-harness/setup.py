from setuptools import setup
setup(
    name='cli-anything-layer',
    version='1.0.0',
    packages=['cli_anything.layer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-layer=cli_anything.layer:cli']},
)
