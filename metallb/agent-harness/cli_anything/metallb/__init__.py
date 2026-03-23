import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('metallb running')
@cli.command()
def start(): click.echo('metallb started')
if __name__ == '__main__': cli()
