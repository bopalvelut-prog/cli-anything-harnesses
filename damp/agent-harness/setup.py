from setuptools import setup
setup(
    name='cli-anything-damp',
    version='1.0.0',
    packages=['cli_anything.damp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-damp=cli_anything.damp:cli']},
)
