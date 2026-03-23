from setuptools import setup
setup(
    name='cli-anything-pscale',
    version='1.0.0',
    packages=['cli_anything.pscale'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pscale=cli_anything.pscale:cli']},
)
