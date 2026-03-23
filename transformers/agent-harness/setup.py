from setuptools import setup
setup(
    name='cli-anything-transformers',
    version='1.0.0',
    packages=['cli_anything.transformers'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transformers=cli_anything.transformers:cli']},
)
