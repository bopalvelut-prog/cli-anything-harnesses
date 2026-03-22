import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def revision(): subprocess.run(['alembic', 'revision', '--autogenerate'])
@cli.command()
def upgrade(): subprocess.run(['alembic', 'upgrade', 'head'])
if __name__ == '__main__': cli()
