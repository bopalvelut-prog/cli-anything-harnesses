from setuptools import setup
setup(
    name='cli-anything-aiven',
    version='1.0.0',
    packages=['cli_anything.aiven'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aiven=cli_anything.aiven:cli']},
)
