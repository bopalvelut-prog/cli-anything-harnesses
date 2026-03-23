from setuptools import setup
setup(
    name='cli-anything-comfort',
    version='1.0.0',
    packages=['cli_anything.comfort'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-comfort=cli_anything.comfort:cli']},
)
