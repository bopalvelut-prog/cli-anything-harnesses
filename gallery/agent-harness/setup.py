from setuptools import setup
setup(
    name='cli-anything-gallery',
    version='1.0.0',
    packages=['cli_anything.gallery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gallery=cli_anything.gallery:cli']},
)
