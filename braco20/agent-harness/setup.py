from setuptools import setup
setup(
    name='cli-anything-braco20',
    version='1.0.0',
    packages=['cli_anything.braco20'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco20=cli_anything.braco20:cli']},
)
