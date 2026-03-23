from setuptools import setup
setup(
    name='cli-anything-rustls',
    version='1.0.0',
    packages=['cli_anything.rustls'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rustls=cli_anything.rustls:cli']},
)
