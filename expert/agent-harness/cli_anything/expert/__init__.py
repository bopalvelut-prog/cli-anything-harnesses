import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('expert running')
@cli.command()
def start(): click.echo('expert started')
if __name__ == '__main__': cli()
