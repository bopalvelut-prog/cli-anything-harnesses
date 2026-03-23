from setuptools import setup
setup(
    name='cli-anything-qlik',
    version='1.0.0',
    packages=['cli_anything.qlik'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qlik=cli_anything.qlik:cli']},
)
