from setuptools import setup
setup(
    name='cli-anything-position',
    version='1.0.0',
    packages=['cli_anything.position'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-position=cli_anything.position:cli']},
)
