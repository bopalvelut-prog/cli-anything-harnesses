from setuptools import setup
setup(
    name='cli-anything-automotive',
    version='1.0.0',
    packages=['cli_anything.automotive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-automotive=cli_anything.automotive:cli']},
)
