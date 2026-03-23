from setuptools import setup
setup(
    name='cli-anything-assets',
    version='1.0.0',
    packages=['cli_anything.assets'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-assets=cli_anything.assets:cli']},
)
