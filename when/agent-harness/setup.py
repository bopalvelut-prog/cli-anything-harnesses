from setuptools import setup
setup(
    name='cli-anything-when',
    version='1.0.0',
    packages=['cli_anything.when'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-when=cli_anything.when:cli']},
)
