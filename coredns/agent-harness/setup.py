from setuptools import setup
setup(
    name='cli-anything-coredns',
    version='1.0.0',
    packages=['cli_anything.coredns'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coredns=cli_anything.coredns:cli']},
)
