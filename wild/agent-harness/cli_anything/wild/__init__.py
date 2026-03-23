import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wild running')
@cli.command()
def start(): click.echo('wild started')
if __name__ == '__main__': cli()
