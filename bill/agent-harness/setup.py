from setuptools import setup
setup(
    name='cli-anything-bill',
    version='1.0.0',
    packages=['cli_anything.bill'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bill=cli_anything.bill:cli']},
)
