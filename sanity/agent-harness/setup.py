from setuptools import setup
setup(
    name='cli-anything-sanity',
    version='1.0.0',
    packages=['cli_anything.sanity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sanity=cli_anything.sanity:cli']},
)
