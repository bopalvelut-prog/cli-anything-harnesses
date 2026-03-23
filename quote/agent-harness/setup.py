from setuptools import setup
setup(
    name='cli-anything-quote',
    version='1.0.0',
    packages=['cli_anything.quote'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quote=cli_anything.quote:cli']},
)
