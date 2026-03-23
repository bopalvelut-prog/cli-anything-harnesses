from setuptools import setup
setup(
    name='cli-anything-material',
    version='1.0.0',
    packages=['cli_anything.material'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-material=cli_anything.material:cli']},
)
