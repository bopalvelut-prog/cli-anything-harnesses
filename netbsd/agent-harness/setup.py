from setuptools import setup
setup(
    name='cli-anything-netbsd',
    version='1.0.0',
    packages=['cli_anything.netbsd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-netbsd=cli_anything.netbsd:cli']},
)
