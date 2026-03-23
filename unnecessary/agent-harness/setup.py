from setuptools import setup
setup(
    name='cli-anything-unnecessary',
    version='1.0.0',
    packages=['cli_anything.unnecessary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unnecessary=cli_anything.unnecessary:cli']},
)
