from setuptools import setup
setup(
    name='cli-anything-kron',
    version='1.0.0',
    packages=['cli_anything.kron'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kron=cli_anything.kron:cli']},
)
