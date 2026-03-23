from setuptools import setup
setup(
    name='cli-anything-manage',
    version='1.0.0',
    packages=['cli_anything.manage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-manage=cli_anything.manage:cli']},
)
