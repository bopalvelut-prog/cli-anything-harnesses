from setuptools import setup
setup(
    name='cli-anything-vultr',
    version='1.0.0',
    packages=['cli_anything.vultr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vultr=cli_anything.vultr:cli']},
)
