import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plant running')
@cli.command()
def start(): click.echo('plant started')
if __name__ == '__main__': cli()
