import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('helmet running')
@cli.command()
def start(): click.echo('helmet started')
if __name__ == '__main__': cli()
