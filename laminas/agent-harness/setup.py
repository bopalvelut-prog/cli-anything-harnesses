from setuptools import setup
setup(
    name='cli-anything-laminas',
    version='1.0.0',
    packages=['cli_anything.laminas'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-laminas=cli_anything.laminas:cli']},
)
