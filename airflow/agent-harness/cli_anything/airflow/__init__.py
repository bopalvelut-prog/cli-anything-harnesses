import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dags(): subprocess.run(['airflow', 'dags', 'list'])
@cli.command()
def trigger(): subprocess.run(['airflow', 'dags', 'trigger'])
if __name__ == '__main__': cli()
