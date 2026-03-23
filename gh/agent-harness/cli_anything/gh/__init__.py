import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gh running')
@cli.command()
def start(): click.echo('gh started')
if __name__ == '__main__': cli()
