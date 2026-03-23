from setuptools import setup
setup(
    name='cli-anything-choose',
    version='1.0.0',
    packages=['cli_anything.choose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-choose=cli_anything.choose:cli']},
)
