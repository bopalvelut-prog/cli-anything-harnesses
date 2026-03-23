from setuptools import setup
setup(
    name='cli-anything-eksctl',
    version='1.0.0',
    packages=['cli_anything.eksctl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eksctl=cli_anything.eksctl:cli']},
)
