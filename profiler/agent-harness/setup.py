from setuptools import setup
setup(
    name='cli-anything-profiler',
    version='1.0.0',
    packages=['cli_anything.profiler'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-profiler=cli_anything.profiler:cli']},
)
