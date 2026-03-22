from setuptools import setup
setup(
    name='cli-anything-directus',
    version='1.0.0',
    packages=['cli_anything.directus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-directus=cli_anything.directus:cli']},
)
