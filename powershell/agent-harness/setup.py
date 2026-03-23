from setuptools import setup
setup(
    name='cli-anything-powershell',
    version='1.0.0',
    packages=['cli_anything.powershell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-powershell=cli_anything.powershell:cli']},
)
