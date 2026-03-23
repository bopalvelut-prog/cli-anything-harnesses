import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('magic running')
@cli.command()
def start(): click.echo('magic started')
if __name__ == '__main__': cli()
