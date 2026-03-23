from setuptools import setup
setup(
    name='cli-anything-kerberos',
    version='1.0.0',
    packages=['cli_anything.kerberos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kerberos=cli_anything.kerberos:cli']},
)
