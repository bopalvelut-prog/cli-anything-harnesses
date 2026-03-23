from setuptools import setup
setup(
    name='cli-anything-art',
    version='1.0.0',
    packages=['cli_anything.art'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-art=cli_anything.art:cli']},
)
