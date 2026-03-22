import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['pg_isready'])
@cli.command()
def backup(): click.echo('Backing up PostgreSQL')
if __name__ == '__main__': cli()
