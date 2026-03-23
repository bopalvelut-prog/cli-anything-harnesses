import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('soup running')
@cli.command()
def start(): click.echo('soup started')
if __name__ == '__main__': cli()
