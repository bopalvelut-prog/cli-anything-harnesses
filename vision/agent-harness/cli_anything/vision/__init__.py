import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vision running')
@cli.command()
def start(): click.echo('vision started')
if __name__ == '__main__': cli()
