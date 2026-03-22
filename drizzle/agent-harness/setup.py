from setuptools import setup
setup(
    name='cli-anything-drizzle',
    version='1.0.0',
    packages=['cli_anything.drizzle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drizzle=cli_anything.drizzle:cli']},
)
