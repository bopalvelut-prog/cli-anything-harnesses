from setuptools import setup
setup(
    name='cli-anything-caddy',
    version='1.0.0',
    packages=['cli_anything.caddy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-caddy=cli_anything.caddy:cli']},
)
