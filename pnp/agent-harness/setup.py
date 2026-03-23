from setuptools import setup
setup(
    name='cli-anything-pnp',
    version='1.0.0',
    packages=['cli_anything.pnp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pnp=cli_anything.pnp:cli']},
)
