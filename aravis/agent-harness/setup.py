from setuptools import setup
setup(
    name='cli-anything-aravis',
    version='1.0.0',
    packages=['cli_anything.aravis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aravis=cli_anything.aravis:cli']},
)
