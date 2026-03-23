from setuptools import setup
setup(
    name='cli-anything-twig',
    version='1.0.0',
    packages=['cli_anything.twig'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-twig=cli_anything.twig:cli']},
)
