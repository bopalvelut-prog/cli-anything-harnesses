from setuptools import setup
setup(
    name='cli-anything-rbac',
    version='1.0.0',
    packages=['cli_anything.rbac'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rbac=cli_anything.rbac:cli']},
)
