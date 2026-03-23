from setuptools import setup
setup(
    name='cli-anything-magma',
    version='1.0.0',
    packages=['cli_anything.magma'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-magma=cli_anything.magma:cli']},
)
