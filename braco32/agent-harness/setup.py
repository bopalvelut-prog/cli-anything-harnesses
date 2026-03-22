from setuptools import setup
setup(
    name='cli-anything-braco32',
    version='1.0.0',
    packages=['cli_anything.braco32'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco32=cli_anything.braco32:cli']},
)
