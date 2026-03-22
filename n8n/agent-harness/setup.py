from setuptools import setup
setup(
    name='cli-anything-n8n',
    version='1.0.0',
    packages=['cli_anything.n8n'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-n8n=cli_anything.n8n:cli']},
)
