from setuptools import setup
setup(
    name='cli-anything-fastify',
    version='1.0.0',
    packages=['cli_anything.fastify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fastify=cli_anything.fastify:cli']},
)
