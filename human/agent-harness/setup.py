from setuptools import setup
setup(
    name='cli-anything-human',
    version='1.0.0',
    packages=['cli_anything.human'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-human=cli_anything.human:cli']},
)
