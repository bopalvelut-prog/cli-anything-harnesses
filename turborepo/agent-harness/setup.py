from setuptools import setup
setup(
    name='cli-anything-turborepo',
    version='1.0.0',
    packages=['cli_anything.turborepo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-turborepo=cli_anything.turborepo:cli']},
)
