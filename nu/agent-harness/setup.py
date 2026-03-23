from setuptools import setup
setup(
    name='cli-anything-nu',
    version='1.0.0',
    packages=['cli_anything.nu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nu=cli_anything.nu:cli']},
)
