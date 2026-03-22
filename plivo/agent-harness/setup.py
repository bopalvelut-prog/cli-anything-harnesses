from setuptools import setup
setup(
    name='cli-anything-plivo',
    version='1.0.0',
    packages=['cli_anything.plivo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plivo=cli_anything.plivo:cli']},
)
