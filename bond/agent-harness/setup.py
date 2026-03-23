from setuptools import setup
setup(
    name='cli-anything-bond',
    version='1.0.0',
    packages=['cli_anything.bond'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bond=cli_anything.bond:cli']},
)
