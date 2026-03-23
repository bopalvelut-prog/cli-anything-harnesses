import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('voice running')
@cli.command()
def start(): click.echo('voice started')
if __name__ == '__main__': cli()
