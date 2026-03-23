from setuptools import setup
setup(
    name='cli-anything-rewrite',
    version='1.0.0',
    packages=['cli_anything.rewrite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rewrite=cli_anything.rewrite:cli']},
)
