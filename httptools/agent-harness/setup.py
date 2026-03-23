from setuptools import setup
setup(
    name='cli-anything-httptools',
    version='1.0.0',
    packages=['cli_anything.httptools'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-httptools=cli_anything.httptools:cli']},
)
