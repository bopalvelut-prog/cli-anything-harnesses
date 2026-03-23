from setuptools import setup
setup(
    name='cli-anything-specification',
    version='1.0.0',
    packages=['cli_anything.specification'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-specification=cli_anything.specification:cli']},
)
