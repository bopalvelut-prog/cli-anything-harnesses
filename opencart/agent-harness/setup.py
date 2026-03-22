from setuptools import setup
setup(
    name='cli-anything-opencart',
    version='1.0.0',
    packages=['cli_anything.opencart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opencart=cli_anything.opencart:cli']},
)
