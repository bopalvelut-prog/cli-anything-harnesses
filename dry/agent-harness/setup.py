from setuptools import setup
setup(
    name='cli-anything-dry',
    version='1.0.0',
    packages=['cli_anything.dry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dry=cli_anything.dry:cli']},
)
