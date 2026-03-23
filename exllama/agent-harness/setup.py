from setuptools import setup
setup(
    name='cli-anything-exllama',
    version='1.0.0',
    packages=['cli_anything.exllama'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-exllama=cli_anything.exllama:cli']},
)
