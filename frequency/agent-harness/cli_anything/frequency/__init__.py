import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('frequency running')
@cli.command()
def start(): click.echo('frequency started')
if __name__ == '__main__': cli()
