from setuptools import setup
setup(
    name='cli-anything-keycdn',
    version='1.0.0',
    packages=['cli_anything.keycdn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keycdn=cli_anything.keycdn:cli']},
)
