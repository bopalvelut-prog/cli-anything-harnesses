import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('uniform running')
@cli.command()
def start(): click.echo('uniform started')
if __name__ == '__main__': cli()
