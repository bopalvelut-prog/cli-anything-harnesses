from setuptools import setup
setup(
    name='cli-anything-tls',
    version='1.0.0',
    packages=['cli_anything.tls'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tls=cli_anything.tls:cli']},
)
