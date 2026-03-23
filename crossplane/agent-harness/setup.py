from setuptools import setup
setup(
    name='cli-anything-crossplane',
    version='1.0.0',
    packages=['cli_anything.crossplane'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crossplane=cli_anything.crossplane:cli']},
)
