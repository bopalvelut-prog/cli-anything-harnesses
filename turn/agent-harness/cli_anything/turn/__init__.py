import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('turn running')
@cli.command()
def start(): click.echo('turn started')
if __name__ == '__main__': cli()
