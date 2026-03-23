from setuptools import setup
setup(
    name='cli-anything-wear',
    version='1.0.0',
    packages=['cli_anything.wear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wear=cli_anything.wear:cli']},
)
