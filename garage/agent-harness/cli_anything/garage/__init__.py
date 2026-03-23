import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('garage running')
@cli.command()
def start(): click.echo('garage started')
if __name__ == '__main__': cli()
