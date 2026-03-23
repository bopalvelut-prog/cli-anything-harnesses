from setuptools import setup
setup(
    name='cli-anything-rapid',
    version='1.0.0',
    packages=['cli_anything.rapid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rapid=cli_anything.rapid:cli']},
)
