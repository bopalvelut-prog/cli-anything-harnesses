from setuptools import setup
setup(
    name='cli-anything-typical',
    version='1.0.0',
    packages=['cli_anything.typical'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-typical=cli_anything.typical:cli']},
)
