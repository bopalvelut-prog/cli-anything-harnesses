from setuptools import setup
setup(
    name='cli-anything-digitalocean',
    version='1.0.0',
    packages=['cli_anything.digitalocean'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-digitalocean=cli_anything.digitalocean:cli']},
)
