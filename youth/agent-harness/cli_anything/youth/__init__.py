import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('youth running')
@cli.command()
def start(): click.echo('youth started')
if __name__ == '__main__': cli()
