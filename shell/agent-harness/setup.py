from setuptools import setup
setup(
    name='cli-anything-shell',
    version='1.0.0',
    packages=['cli_anything.shell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shell=cli_anything.shell:cli']},
)
