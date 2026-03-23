from setuptools import setup
setup(
    name='cli-anything-astro',
    version='1.0.0',
    packages=['cli_anything.astro'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-astro=cli_anything.astro:cli']},
)
