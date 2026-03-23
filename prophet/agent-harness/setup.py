from setuptools import setup
setup(
    name='cli-anything-prophet',
    version='1.0.0',
    packages=['cli_anything.prophet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prophet=cli_anything.prophet:cli']},
)
