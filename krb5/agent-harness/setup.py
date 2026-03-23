from setuptools import setup
setup(
    name='cli-anything-krb5',
    version='1.0.0',
    packages=['cli_anything.krb5'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-krb5=cli_anything.krb5:cli']},
)
