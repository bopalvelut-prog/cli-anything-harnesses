import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('march running')
@cli.command()
def start(): click.echo('march started')
if __name__ == '__main__': cli()
