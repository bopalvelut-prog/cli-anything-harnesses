from setuptools import setup
setup(
    name='cli-anything-honor',
    version='1.0.0',
    packages=['cli_anything.honor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-honor=cli_anything.honor:cli']},
)
