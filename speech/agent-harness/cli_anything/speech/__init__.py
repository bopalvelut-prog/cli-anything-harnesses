import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('speech running')
@cli.command()
def start(): click.echo('speech started')
if __name__ == '__main__': cli()
