from setuptools import setup
setup(
    name='cli-anything-northern',
    version='1.0.0',
    packages=['cli_anything.northern'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-northern=cli_anything.northern:cli']},
)
