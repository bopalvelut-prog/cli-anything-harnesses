from setuptools import setup
setup(
    name='cli-anything-graphene',
    version='1.0.0',
    packages=['cli_anything.graphene'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-graphene=cli_anything.graphene:cli']},
)
