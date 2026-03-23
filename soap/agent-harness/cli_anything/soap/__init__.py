import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('soap running')
@cli.command()
def start(): click.echo('soap started')
if __name__ == '__main__': cli()
