import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ligo running')
@cli.command()
def start(): click.echo('ligo started')
if __name__ == '__main__': cli()
