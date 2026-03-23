from setuptools import setup
setup(
    name='cli-anything-whatever',
    version='1.0.0',
    packages=['cli_anything.whatever'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-whatever=cli_anything.whatever:cli']},
)
