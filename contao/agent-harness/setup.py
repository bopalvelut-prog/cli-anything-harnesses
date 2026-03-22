from setuptools import setup
setup(
    name='cli-anything-contao',
    version='1.0.0',
    packages=['cli_anything.contao'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-contao=cli_anything.contao:cli']},
)
