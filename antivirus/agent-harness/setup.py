from setuptools import setup
setup(
    name='cli-anything-antivirus',
    version='1.0.0',
    packages=['cli_anything.antivirus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-antivirus=cli_anything.antivirus:cli']},
)
