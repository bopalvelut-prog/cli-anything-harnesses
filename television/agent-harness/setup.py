from setuptools import setup
setup(
    name='cli-anything-television',
    version='1.0.0',
    packages=['cli_anything.television'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-television=cli_anything.television:cli']},
)
