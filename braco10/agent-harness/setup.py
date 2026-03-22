from setuptools import setup
setup(
    name='cli-anything-braco10',
    version='1.0.0',
    packages=['cli_anything.braco10'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco10=cli_anything.braco10:cli']},
)
