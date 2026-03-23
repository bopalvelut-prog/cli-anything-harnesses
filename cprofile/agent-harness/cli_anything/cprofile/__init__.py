import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cprofile running')
@cli.command()
def start(): click.echo('cprofile started')
if __name__ == '__main__': cli()
