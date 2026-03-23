from setuptools import setup
setup(
    name='cli-anything-better',
    version='1.0.0',
    packages=['cli_anything.better'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-better=cli_anything.better:cli']},
)
