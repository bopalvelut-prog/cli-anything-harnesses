from setuptools import setup
setup(
    name='cli-anything-modular',
    version='1.0.0',
    packages=['cli_anything.modular'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-modular=cli_anything.modular:cli']},
)
