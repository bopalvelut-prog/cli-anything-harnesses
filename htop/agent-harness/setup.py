from setuptools import setup
setup(
    name='cli-anything-htop',
    version='1.0.0',
    packages=['cli_anything.htop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-htop=cli_anything.htop:cli']},
)
