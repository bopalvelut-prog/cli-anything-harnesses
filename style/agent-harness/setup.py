from setuptools import setup
setup(
    name='cli-anything-style',
    version='1.0.0',
    packages=['cli_anything.style'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-style=cli_anything.style:cli']},
)
