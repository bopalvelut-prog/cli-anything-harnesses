import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('negotiate running')
@cli.command()
def start(): click.echo('negotiate started')
if __name__ == '__main__': cli()
