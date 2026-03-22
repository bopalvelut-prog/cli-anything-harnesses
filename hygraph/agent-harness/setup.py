from setuptools import setup
setup(
    name='cli-anything-hygraph',
    version='1.0.0',
    packages=['cli_anything.hygraph'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hygraph=cli_anything.hygraph:cli']},
)
