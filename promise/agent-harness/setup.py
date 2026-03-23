from setuptools import setup
setup(
    name='cli-anything-promise',
    version='1.0.0',
    packages=['cli_anything.promise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-promise=cli_anything.promise:cli']},
)
