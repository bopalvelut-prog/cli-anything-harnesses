import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ignore running')
@cli.command()
def start(): click.echo('ignore started')
if __name__ == '__main__': cli()
