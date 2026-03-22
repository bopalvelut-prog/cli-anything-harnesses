from setuptools import setup
setup(
    name='cli-anything-svelte',
    version='1.0.0',
    packages=['cli_anything.svelte'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-svelte=cli_anything.svelte:cli']},
)
