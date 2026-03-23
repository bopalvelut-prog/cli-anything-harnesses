from setuptools import setup
setup(
    name='cli-anything-tender',
    version='1.0.0',
    packages=['cli_anything.tender'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tender=cli_anything.tender:cli']},
)
