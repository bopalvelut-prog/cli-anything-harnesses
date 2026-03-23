import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('radio running')
@cli.command()
def start(): click.echo('radio started')
if __name__ == '__main__': cli()
