import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aurora_mysql running')
@cli.command()
def start(): click.echo('aurora_mysql started')
if __name__ == '__main__': cli()
