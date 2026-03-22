from setuptools import setup
setup(
    name='cli-anything-braco30',
    version='1.0.0',
    packages=['cli_anything.braco30'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco30=cli_anything.braco30:cli']},
)
