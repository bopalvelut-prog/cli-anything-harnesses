from setuptools import setup
setup(
    name='cli-anything-httpx',
    version='1.0.0',
    packages=['cli_anything.httpx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-httpx=cli_anything.httpx:cli']},
)
