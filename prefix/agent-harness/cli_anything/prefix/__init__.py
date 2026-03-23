import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prefix running')
@cli.command()
def start(): click.echo('prefix started')
if __name__ == '__main__': cli()
