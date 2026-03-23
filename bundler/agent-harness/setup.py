from setuptools import setup
setup(
    name='cli-anything-bundler',
    version='1.0.0',
    packages=['cli_anything.bundler'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bundler=cli_anything.bundler:cli']},
)
