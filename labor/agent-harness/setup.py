from setuptools import setup
setup(
    name='cli-anything-labor',
    version='1.0.0',
    packages=['cli_anything.labor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-labor=cli_anything.labor:cli']},
)
