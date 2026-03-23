from setuptools import setup
setup(
    name='cli-anything-rspec',
    version='1.0.0',
    packages=['cli_anything.rspec'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rspec=cli_anything.rspec:cli']},
)
