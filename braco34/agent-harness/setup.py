from setuptools import setup
setup(
    name='cli-anything-braco34',
    version='1.0.0',
    packages=['cli_anything.braco34'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco34=cli_anything.braco34:cli']},
)
