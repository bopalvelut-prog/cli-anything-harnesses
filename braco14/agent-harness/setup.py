from setuptools import setup
setup(
    name='cli-anything-braco14',
    version='1.0.0',
    packages=['cli_anything.braco14'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco14=cli_anything.braco14:cli']},
)
