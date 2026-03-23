from setuptools import setup
setup(
    name='cli-anything-foreign',
    version='1.0.0',
    packages=['cli_anything.foreign'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-foreign=cli_anything.foreign:cli']},
)
