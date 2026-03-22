from setuptools import setup
setup(
    name='cli-anything-helm',
    version='1.0.0',
    packages=['cli_anything.helm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-helm=cli_anything.helm:cli']},
)
