from setuptools import setup
setup(
    name='cli-anything-prisma',
    version='1.0.0',
    packages=['cli_anything.prisma'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prisma=cli_anything.prisma:cli']},
)
