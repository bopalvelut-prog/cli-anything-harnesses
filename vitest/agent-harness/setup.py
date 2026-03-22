from setuptools import setup
setup(
    name='cli-anything-vitest',
    version='1.0.0',
    packages=['cli_anything.vitest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vitest=cli_anything.vitest:cli']},
)
