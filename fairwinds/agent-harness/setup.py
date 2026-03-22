from setuptools import setup
setup(
    name='cli-anything-fairwinds',
    version='1.0.0',
    packages=['cli_anything.fairwinds'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fairwinds=cli_anything.fairwinds:cli']},
)
