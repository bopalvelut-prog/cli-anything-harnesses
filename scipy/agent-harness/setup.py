from setuptools import setup
setup(
    name='cli-anything-scipy',
    version='1.0.0',
    packages=['cli_anything.scipy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scipy=cli_anything.scipy:cli']},
)
