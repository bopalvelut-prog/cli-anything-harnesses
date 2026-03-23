import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_worklink running')
@cli.command()
def start(): click.echo('amazon_worklink started')
if __name__ == '__main__': cli()
