from setuptools import setup
setup(
    name='cli-anything-resistance',
    version='1.0.0',
    packages=['cli_anything.resistance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resistance=cli_anything.resistance:cli']},
)
