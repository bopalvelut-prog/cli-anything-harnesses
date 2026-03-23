from setuptools import setup
setup(
    name='cli-anything-nss',
    version='1.0.0',
    packages=['cli_anything.nss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nss=cli_anything.nss:cli']},
)
