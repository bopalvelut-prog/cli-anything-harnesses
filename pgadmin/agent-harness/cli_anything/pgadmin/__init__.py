import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pgadmin running')
@cli.command()
def start(): click.echo('pgadmin started')
if __name__ == '__main__': cli()
