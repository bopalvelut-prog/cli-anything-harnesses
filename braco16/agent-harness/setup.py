from setuptools import setup
setup(
    name='cli-anything-braco16',
    version='1.0.0',
    packages=['cli_anything.braco16'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco16=cli_anything.braco16:cli']},
)
