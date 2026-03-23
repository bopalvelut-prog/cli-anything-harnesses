from setuptools import setup
setup(
    name='cli-anything-etlegacy',
    version='1.0.0',
    packages=['cli_anything.etlegacy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-etlegacy=cli_anything.etlegacy:cli']},
)
