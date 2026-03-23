from setuptools import setup
setup(
    name='cli-anything-contract',
    version='1.0.0',
    packages=['cli_anything.contract'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-contract=cli_anything.contract:cli']},
)
