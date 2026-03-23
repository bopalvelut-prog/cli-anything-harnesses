import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('count running')
@cli.command()
def start(): click.echo('count started')
if __name__ == '__main__': cli()
