import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lovely running')
@cli.command()
def start(): click.echo('lovely started')
if __name__ == '__main__': cli()
