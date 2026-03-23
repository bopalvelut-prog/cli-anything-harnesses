from setuptools import setup
setup(
    name='cli-anything-rekor',
    version='1.0.0',
    packages=['cli_anything.rekor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rekor=cli_anything.rekor:cli']},
)
