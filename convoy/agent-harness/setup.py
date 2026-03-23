from setuptools import setup
setup(
    name='cli-anything-convoy',
    version='1.0.0',
    packages=['cli_anything.convoy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-convoy=cli_anything.convoy:cli']},
)
