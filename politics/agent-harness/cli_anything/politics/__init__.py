import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('politics running')
@cli.command()
def start(): click.echo('politics started')
if __name__ == '__main__': cli()
