import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('remain running')
@cli.command()
def start(): click.echo('remain started')
if __name__ == '__main__': cli()
