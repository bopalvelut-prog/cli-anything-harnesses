from setuptools import setup
setup(
    name='cli-anything-braco40',
    version='1.0.0',
    packages=['cli_anything.braco40'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco40=cli_anything.braco40:cli']},
)
