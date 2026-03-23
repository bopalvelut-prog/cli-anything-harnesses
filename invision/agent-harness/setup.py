from setuptools import setup
setup(
    name='cli-anything-invision',
    version='1.0.0',
    packages=['cli_anything.invision'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-invision=cli_anything.invision:cli']},
)
