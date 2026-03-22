from setuptools import setup
setup(
    name='cli-anything-braco26',
    version='1.0.0',
    packages=['cli_anything.braco26'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco26=cli_anything.braco26:cli']},
)
