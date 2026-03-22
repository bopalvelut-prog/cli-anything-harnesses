from setuptools import setup
setup(
    name='cli-anything-duplicity',
    version='1.0.0',
    packages=['cli_anything.duplicity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-duplicity=cli_anything.duplicity:cli']},
)
