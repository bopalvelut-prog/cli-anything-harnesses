from setuptools import setup
setup(
    name='cli-anything-flux',
    version='1.0.0',
    packages=['cli_anything.flux'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flux=cli_anything.flux:cli']},
)
