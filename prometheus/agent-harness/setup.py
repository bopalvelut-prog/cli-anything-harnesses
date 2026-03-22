from setuptools import setup
setup(
    name='cli-anything-prometheus',
    version='1.0.0',
    packages=['cli_anything.prometheus'],
    install_requires=['click', 'requests'],
    entry_points={'console_scripts': ['cli-anything-prometheus=cli_anything.prometheus:cli']},
)
