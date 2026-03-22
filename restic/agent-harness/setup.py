from setuptools import setup
setup(
    name='cli-anything-restic',
    version='1.0.0',
    packages=['cli_anything.restic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-restic=cli_anything.restic:cli']},
)
