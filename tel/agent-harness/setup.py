from setuptools import setup
setup(
    name='cli-anything-tel',
    version='1.0.0',
    packages=['cli_anything.tel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tel=cli_anything.tel:cli']},
)
