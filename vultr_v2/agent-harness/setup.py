from setuptools import setup
setup(
    name='cli-anything-vultr_v2',
    version='1.0.0',
    packages=['cli_anything.vultr_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vultr_v2=cli_anything.vultr_v2:cli']},
)
