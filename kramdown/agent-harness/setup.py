from setuptools import setup
setup(
    name='cli-anything-kramdown',
    version='1.0.0',
    packages=['cli_anything.kramdown'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kramdown=cli_anything.kramdown:cli']},
)
