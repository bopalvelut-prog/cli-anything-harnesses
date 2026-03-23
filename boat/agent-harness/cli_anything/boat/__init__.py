import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('boat running')
@cli.command()
def start(): click.echo('boat started')
if __name__ == '__main__': cli()
