from setuptools import setup
setup(
    name='cli-anything-inspec',
    version='1.0.0',
    packages=['cli_anything.inspec'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inspec=cli_anything.inspec:cli']},
)
