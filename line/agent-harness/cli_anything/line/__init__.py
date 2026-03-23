import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('line running')
@cli.command()
def start(): click.echo('line started')
if __name__ == '__main__': cli()
