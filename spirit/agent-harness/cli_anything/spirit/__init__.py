import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spirit running')
@cli.command()
def start(): click.echo('spirit started')
if __name__ == '__main__': cli()
