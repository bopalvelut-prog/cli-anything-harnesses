import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('logger running')
@cli.command()
def start(): click.echo('logger started')
if __name__ == '__main__': cli()
