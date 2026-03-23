import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tau running')
@cli.command()
def start(): click.echo('tau started')
if __name__ == '__main__': cli()
