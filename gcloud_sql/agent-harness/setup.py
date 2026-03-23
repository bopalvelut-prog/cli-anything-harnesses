from setuptools import setup
setup(
    name='cli-anything-gcloud_sql',
    version='1.0.0',
    packages=['cli_anything.gcloud_sql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcloud_sql=cli_anything.gcloud_sql:cli']},
)
