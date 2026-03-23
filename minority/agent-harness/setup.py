from setuptools import setup
setup(
    name='cli-anything-minority',
    version='1.0.0',
    packages=['cli_anything.minority'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-minority=cli_anything.minority:cli']},
)
