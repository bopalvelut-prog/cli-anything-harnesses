from setuptools import setup
setup(
    name='cli-anything-augmented',
    version='1.0.0',
    packages=['cli_anything.augmented'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-augmented=cli_anything.augmented:cli']},
)
