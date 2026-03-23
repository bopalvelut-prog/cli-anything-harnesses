from setuptools import setup
setup(
    name='cli-anything-shoulder',
    version='1.0.0',
    packages=['cli_anything.shoulder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shoulder=cli_anything.shoulder:cli']},
)
