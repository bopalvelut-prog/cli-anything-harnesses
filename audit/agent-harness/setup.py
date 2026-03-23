from setuptools import setup
setup(
    name='cli-anything-audit',
    version='1.0.0',
    packages=['cli_anything.audit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-audit=cli_anything.audit:cli']},
)
