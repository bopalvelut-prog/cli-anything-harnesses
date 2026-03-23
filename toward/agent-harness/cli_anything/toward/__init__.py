import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('toward running')
@cli.command()
def start(): click.echo('toward started')
if __name__ == '__main__': cli()
