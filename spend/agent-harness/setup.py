from setuptools import setup
setup(
    name='cli-anything-spend',
    version='1.0.0',
    packages=['cli_anything.spend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spend=cli_anything.spend:cli']},
)
