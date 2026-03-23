from setuptools import setup
setup(
    name='cli-anything-kubesec',
    version='1.0.0',
    packages=['cli_anything.kubesec'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubesec=cli_anything.kubesec:cli']},
)
