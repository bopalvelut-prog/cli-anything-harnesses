import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('foot running')
@cli.command()
def start(): click.echo('foot started')
if __name__ == '__main__': cli()
