from setuptools import setup
setup(
    name='cli-anything-mikrotik',
    version='1.0.0',
    packages=['cli_anything.mikrotik'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mikrotik=cli_anything.mikrotik:cli']},
)
