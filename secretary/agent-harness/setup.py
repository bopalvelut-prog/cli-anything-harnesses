from setuptools import setup
setup(
    name='cli-anything-secretary',
    version='1.0.0',
    packages=['cli_anything.secretary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-secretary=cli_anything.secretary:cli']},
)
