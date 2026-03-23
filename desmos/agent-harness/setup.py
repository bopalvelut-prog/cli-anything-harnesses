from setuptools import setup
setup(
    name='cli-anything-desmos',
    version='1.0.0',
    packages=['cli_anything.desmos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-desmos=cli_anything.desmos:cli']},
)
