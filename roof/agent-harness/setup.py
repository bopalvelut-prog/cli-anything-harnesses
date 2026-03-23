from setuptools import setup
setup(
    name='cli-anything-roof',
    version='1.0.0',
    packages=['cli_anything.roof'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-roof=cli_anything.roof:cli']},
)
