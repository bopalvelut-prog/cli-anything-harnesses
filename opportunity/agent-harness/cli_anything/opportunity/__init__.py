import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('opportunity running')
@cli.command()
def start(): click.echo('opportunity started')
if __name__ == '__main__': cli()
