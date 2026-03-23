from setuptools import setup
setup(
    name='cli-anything-github',
    version='1.0.0',
    packages=['cli_anything.github'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-github=cli_anything.github:cli']},
)
