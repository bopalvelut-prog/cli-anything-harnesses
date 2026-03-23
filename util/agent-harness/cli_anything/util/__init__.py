import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('util running')
@cli.command()
def start(): click.echo('util started')
if __name__ == '__main__': cli()
