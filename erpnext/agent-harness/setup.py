from setuptools import setup
setup(
    name='cli-anything-erpnext',
    version='1.0.0',
    packages=['cli_anything.erpnext'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-erpnext=cli_anything.erpnext:cli']},
)
