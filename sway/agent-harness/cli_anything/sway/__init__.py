import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sway running')
@cli.command()
def start(): click.echo('sway started')
if __name__ == '__main__': cli()
