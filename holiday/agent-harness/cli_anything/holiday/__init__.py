import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('holiday running')
@cli.command()
def start(): click.echo('holiday started')
if __name__ == '__main__': cli()
