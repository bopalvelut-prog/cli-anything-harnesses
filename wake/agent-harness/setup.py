from setuptools import setup
setup(
    name='cli-anything-wake',
    version='1.0.0',
    packages=['cli_anything.wake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wake=cli_anything.wake:cli']},
)
