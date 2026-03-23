import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('solid running')
@cli.command()
def start(): click.echo('solid started')
if __name__ == '__main__': cli()
