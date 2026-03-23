import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('appsync running')
@cli.command()
def start(): click.echo('appsync started')
if __name__ == '__main__': cli()
