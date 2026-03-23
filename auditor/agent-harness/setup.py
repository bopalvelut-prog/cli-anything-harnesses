from setuptools import setup
setup(
    name='cli-anything-auditor',
    version='1.0.0',
    packages=['cli_anything.auditor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-auditor=cli_anything.auditor:cli']},
)
