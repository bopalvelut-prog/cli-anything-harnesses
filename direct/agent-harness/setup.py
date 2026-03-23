from setuptools import setup
setup(
    name='cli-anything-direct',
    version='1.0.0',
    packages=['cli_anything.direct'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-direct=cli_anything.direct:cli']},
)
