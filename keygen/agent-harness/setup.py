from setuptools import setup
setup(
    name='cli-anything-keygen',
    version='1.0.0',
    packages=['cli_anything.keygen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keygen=cli_anything.keygen:cli']},
)
