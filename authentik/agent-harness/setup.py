from setuptools import setup
setup(
    name='cli-anything-authentik',
    version='1.0.0',
    packages=['cli_anything.authentik'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-authentik=cli_anything.authentik:cli']},
)
