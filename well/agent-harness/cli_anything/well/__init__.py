import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('well running')
@cli.command()
def start(): click.echo('well started')
if __name__ == '__main__': cli()
