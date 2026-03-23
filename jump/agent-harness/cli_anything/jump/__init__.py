import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jump running')
@cli.command()
def start(): click.echo('jump started')
if __name__ == '__main__': cli()
