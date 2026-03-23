from setuptools import setup
setup(
    name='cli-anything-readthedocs',
    version='1.0.0',
    packages=['cli_anything.readthedocs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-readthedocs=cli_anything.readthedocs:cli']},
)
