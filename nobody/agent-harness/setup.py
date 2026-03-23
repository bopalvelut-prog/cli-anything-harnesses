from setuptools import setup
setup(
    name='cli-anything-nobody',
    version='1.0.0',
    packages=['cli_anything.nobody'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nobody=cli_anything.nobody:cli']},
)
