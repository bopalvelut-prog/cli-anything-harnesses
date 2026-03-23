from setuptools import setup
setup(
    name='cli-anything-tin',
    version='1.0.0',
    packages=['cli_anything.tin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tin=cli_anything.tin:cli']},
)
