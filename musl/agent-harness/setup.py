from setuptools import setup
setup(
    name='cli-anything-musl',
    version='1.0.0',
    packages=['cli_anything.musl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-musl=cli_anything.musl:cli']},
)
