import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('odbc running')
@cli.command()
def start(): click.echo('odbc started')
if __name__ == '__main__': cli()
