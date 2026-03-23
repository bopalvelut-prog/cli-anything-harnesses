import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('relatively running')
@cli.command()
def start(): click.echo('relatively started')
if __name__ == '__main__': cli()
