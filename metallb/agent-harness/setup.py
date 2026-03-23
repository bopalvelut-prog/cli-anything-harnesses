from setuptools import setup
setup(
    name='cli-anything-metallb',
    version='1.0.0',
    packages=['cli_anything.metallb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-metallb=cli_anything.metallb:cli']},
)
