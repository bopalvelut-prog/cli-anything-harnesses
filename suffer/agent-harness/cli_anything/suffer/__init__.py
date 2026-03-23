import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('suffer running')
@cli.command()
def start(): click.echo('suffer started')
if __name__ == '__main__': cli()
