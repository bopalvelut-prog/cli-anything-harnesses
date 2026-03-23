import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lorawan running')
@cli.command()
def start(): click.echo('lorawan started')
if __name__ == '__main__': cli()
