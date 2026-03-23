import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ransack running')
@cli.command()
def start(): click.echo('ransack started')
if __name__ == '__main__': cli()
