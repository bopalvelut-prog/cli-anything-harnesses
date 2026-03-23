import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('orange running')
@cli.command()
def start(): click.echo('orange started')
if __name__ == '__main__': cli()
