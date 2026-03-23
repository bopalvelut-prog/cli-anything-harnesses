from setuptools import setup
setup(
    name='cli-anything-twelve',
    version='1.0.0',
    packages=['cli_anything.twelve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-twelve=cli_anything.twelve:cli']},
)
