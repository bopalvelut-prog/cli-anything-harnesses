import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('recognize running')
@cli.command()
def start(): click.echo('recognize started')
if __name__ == '__main__': cli()
