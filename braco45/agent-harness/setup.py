from setuptools import setup
setup(
    name='cli-anything-braco45',
    version='1.0.0',
    packages=['cli_anything.braco45'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco45=cli_anything.braco45:cli']},
)
