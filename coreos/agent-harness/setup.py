from setuptools import setup
setup(
    name='cli-anything-coreos',
    version='1.0.0',
    packages=['cli_anything.coreos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coreos=cli_anything.coreos:cli']},
)
