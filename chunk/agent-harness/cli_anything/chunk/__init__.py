import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chunk running')
@cli.command()
def start(): click.echo('chunk started')
if __name__ == '__main__': cli()
