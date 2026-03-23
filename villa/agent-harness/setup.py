from setuptools import setup
setup(
    name='cli-anything-villa',
    version='1.0.0',
    packages=['cli_anything.villa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-villa=cli_anything.villa:cli']},
)
