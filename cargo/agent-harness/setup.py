from setuptools import setup
setup(
    name='cli-anything-cargo',
    version='1.0.0',
    packages=['cli_anything.cargo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cargo=cli_anything.cargo:cli']},
)
