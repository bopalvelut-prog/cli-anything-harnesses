from setuptools import setup
setup(
    name='cli-anything-jax',
    version='1.0.0',
    packages=['cli_anything.jax'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jax=cli_anything.jax:cli']},
)
