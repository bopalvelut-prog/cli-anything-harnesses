from setuptools import setup
setup(
    name='cli-anything-assurance',
    version='1.0.0',
    packages=['cli_anything.assurance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-assurance=cli_anything.assurance:cli']},
)
