from setuptools import setup
setup(
    name='cli-anything-codesys',
    version='1.0.0',
    packages=['cli_anything.codesys'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codesys=cli_anything.codesys:cli']},
)
