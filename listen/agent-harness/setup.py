from setuptools import setup
setup(
    name='cli-anything-listen',
    version='1.0.0',
    packages=['cli_anything.listen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-listen=cli_anything.listen:cli']},
)
