from setuptools import setup
setup(
    name='cli-anything-compete',
    version='1.0.0',
    packages=['cli_anything.compete'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-compete=cli_anything.compete:cli']},
)
