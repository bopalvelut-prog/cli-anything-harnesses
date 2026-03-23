import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('copyleft running')
@cli.command()
def start(): click.echo('copyleft started')
if __name__ == '__main__': cli()
