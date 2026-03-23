from setuptools import setup
setup(
    name='cli-anything-stellar',
    version='1.0.0',
    packages=['cli_anything.stellar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stellar=cli_anything.stellar:cli']},
)
