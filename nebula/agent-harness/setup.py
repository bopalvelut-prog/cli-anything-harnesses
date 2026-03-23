from setuptools import setup
setup(
    name='cli-anything-nebula',
    version='1.0.0',
    packages=['cli_anything.nebula'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nebula=cli_anything.nebula:cli']},
)
