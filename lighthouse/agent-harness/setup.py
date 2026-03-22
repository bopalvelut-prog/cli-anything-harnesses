from setuptools import setup
setup(
    name='cli-anything-lighthouse',
    version='1.0.0',
    packages=['cli_anything.lighthouse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lighthouse=cli_anything.lighthouse:cli']},
)
