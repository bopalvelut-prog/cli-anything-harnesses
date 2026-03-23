from setuptools import setup
setup(
    name='cli-anything-wright',
    version='1.0.0',
    packages=['cli_anything.wright'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wright=cli_anything.wright:cli']},
)
