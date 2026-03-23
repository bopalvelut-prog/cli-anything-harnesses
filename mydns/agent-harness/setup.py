from setuptools import setup
setup(
    name='cli-anything-mydns',
    version='1.0.0',
    packages=['cli_anything.mydns'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mydns=cli_anything.mydns:cli']},
)
