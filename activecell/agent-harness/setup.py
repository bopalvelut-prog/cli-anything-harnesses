from setuptools import setup
setup(
    name='cli-anything-activecell',
    version='1.0.0',
    packages=['cli_anything.activecell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-activecell=cli_anything.activecell:cli']},
)
