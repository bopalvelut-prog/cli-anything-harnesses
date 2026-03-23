from setuptools import setup
setup(
    name='cli-anything-dero',
    version='1.0.0',
    packages=['cli_anything.dero'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dero=cli_anything.dero:cli']},
)
