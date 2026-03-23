from setuptools import setup
setup(
    name='cli-anything-velero',
    version='1.0.0',
    packages=['cli_anything.velero'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-velero=cli_anything.velero:cli']},
)
