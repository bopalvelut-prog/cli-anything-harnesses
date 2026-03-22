from setuptools import setup
setup(
    name='cli-anything-adonis',
    version='1.0.0',
    packages=['cli_anything.adonis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adonis=cli_anything.adonis:cli']},
)
