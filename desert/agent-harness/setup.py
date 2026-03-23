from setuptools import setup
setup(
    name='cli-anything-desert',
    version='1.0.0',
    packages=['cli_anything.desert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-desert=cli_anything.desert:cli']},
)
