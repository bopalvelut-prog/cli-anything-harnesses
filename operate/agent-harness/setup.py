from setuptools import setup
setup(
    name='cli-anything-operate',
    version='1.0.0',
    packages=['cli_anything.operate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-operate=cli_anything.operate:cli']},
)
