import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hate running')
@cli.command()
def start(): click.echo('hate started')
if __name__ == '__main__': cli()
