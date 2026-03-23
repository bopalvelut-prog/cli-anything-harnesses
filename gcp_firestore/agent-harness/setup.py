from setuptools import setup
setup(
    name='cli-anything-gcp_firestore',
    version='1.0.0',
    packages=['cli_anything.gcp_firestore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_firestore=cli_anything.gcp_firestore:cli']},
)
