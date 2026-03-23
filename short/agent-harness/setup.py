from setuptools import setup
setup(
    name='cli-anything-short',
    version='1.0.0',
    packages=['cli_anything.short'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-short=cli_anything.short:cli']},
)
