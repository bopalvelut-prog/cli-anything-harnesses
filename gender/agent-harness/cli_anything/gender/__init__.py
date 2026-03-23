import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gender running')
@cli.command()
def start(): click.echo('gender started')
if __name__ == '__main__': cli()
