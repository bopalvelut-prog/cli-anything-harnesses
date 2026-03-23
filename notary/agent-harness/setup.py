from setuptools import setup
setup(
    name='cli-anything-notary',
    version='1.0.0',
    packages=['cli_anything.notary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-notary=cli_anything.notary:cli']},
)
