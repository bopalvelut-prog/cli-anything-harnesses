from setuptools import setup
setup(
    name='cli-anything-bun_runtime',
    version='1.0.0',
    packages=['cli_anything.bun_runtime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bun_runtime=cli_anything.bun_runtime:cli']},
)
