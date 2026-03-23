import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('issue running')
@cli.command()
def start(): click.echo('issue started')
if __name__ == '__main__': cli()
