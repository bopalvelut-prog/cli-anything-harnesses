import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('router running')
@cli.command()
def start(): click.echo('router started')
if __name__ == '__main__': cli()
