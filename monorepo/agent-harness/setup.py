from setuptools import setup
setup(
    name='cli-anything-monorepo',
    version='1.0.0',
    packages=['cli_anything.monorepo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-monorepo=cli_anything.monorepo:cli']},
)
