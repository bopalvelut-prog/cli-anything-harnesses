from setuptools import setup
setup(
    name='cli-anything-braco47',
    version='1.0.0',
    packages=['cli_anything.braco47'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco47=cli_anything.braco47:cli']},
)
