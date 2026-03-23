import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('label running')
@cli.command()
def start(): click.echo('label started')
if __name__ == '__main__': cli()
