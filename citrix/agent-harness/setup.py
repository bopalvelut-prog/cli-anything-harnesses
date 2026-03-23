from setuptools import setup
setup(
    name='cli-anything-citrix',
    version='1.0.0',
    packages=['cli_anything.citrix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-citrix=cli_anything.citrix:cli']},
)
