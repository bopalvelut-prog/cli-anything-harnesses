import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('compare running')
@cli.command()
def start(): click.echo('compare started')
if __name__ == '__main__': cli()
