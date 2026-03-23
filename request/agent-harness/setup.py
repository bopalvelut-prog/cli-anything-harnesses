from setuptools import setup
setup(
    name='cli-anything-request',
    version='1.0.0',
    packages=['cli_anything.request'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-request=cli_anything.request:cli']},
)
