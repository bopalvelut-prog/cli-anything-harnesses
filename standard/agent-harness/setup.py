from setuptools import setup
setup(
    name='cli-anything-standard',
    version='1.0.0',
    packages=['cli_anything.standard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-standard=cli_anything.standard:cli']},
)
