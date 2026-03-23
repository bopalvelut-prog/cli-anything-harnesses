import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('omnibus running')
@cli.command()
def start(): click.echo('omnibus started')
if __name__ == '__main__': cli()
